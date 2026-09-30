#!/usr/bin/env python3
"""Validate a native 3:4 cover and resize the whole image to 1080x1440."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image


TARGET_SIZE = (1080, 1440)
TARGET_RATIO = 3 / 4


class CoverFinalizationError(ValueError):
    """Raised when a cover cannot be finalized without cropping."""


def finalize_cover(
    source: Path,
    destination: Path,
    tolerance: float = 0.002,
    overwrite: bool = False,
) -> dict:
    """Resize an almost-3:4 image in full and return machine-readable metadata."""
    source = Path(source)
    destination = Path(destination)

    if not source.is_file():
        raise CoverFinalizationError(f"source image does not exist: {source}")
    if destination.suffix.lower() != ".png":
        raise CoverFinalizationError("destination must use the .png extension for PNG output")
    if destination.exists() and not overwrite:
        raise CoverFinalizationError(f"destination already exists: {destination}")
    if tolerance < 0:
        raise CoverFinalizationError("tolerance must be zero or greater")

    with Image.open(source) as image:
        source_size = image.size
        width, height = source_size
        ratio_error = abs((width / height) - TARGET_RATIO)
        if ratio_error > tolerance:
            raise CoverFinalizationError(
                f"source must be native 3:4; got {width}x{height} "
                f"(ratio error {ratio_error:.6f}, tolerance {tolerance:.6f})"
            )

        finalized = image.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
        destination.parent.mkdir(parents=True, exist_ok=True)
        finalized.save(destination, format="PNG")

    return {
        "source": str(source.resolve()),
        "destination": str(destination.resolve()),
        "source_size": list(source_size),
        "final_size": list(TARGET_SIZE),
        "ratio_error": ratio_error,
        "cropped": False,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate a native 3:4 image and resize it to 1080x1440 PNG without cropping."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--tolerance", type=float, default=0.002)
    parser.add_argument("--overwrite", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = finalize_cover(
            args.source,
            args.destination,
            tolerance=args.tolerance,
            overwrite=args.overwrite,
        )
    except (CoverFinalizationError, OSError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1

    print(json.dumps({"ok": True, **result}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
