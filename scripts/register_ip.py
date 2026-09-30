#!/usr/bin/env python3
"""Register a replaceable person IP package from explicit local references."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

from PIL import Image, UnidentifiedImageError


SLUG_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}$")
SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


class IPRegistrationError(ValueError):
    """Raised when an IP package cannot be created safely."""


def _validate_reference(path: Path) -> None:
    if not path.is_file():
        raise IPRegistrationError(f"reference image does not exist: {path}")
    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise IPRegistrationError(f"unsupported reference image format: {path.suffix}")
    try:
        with Image.open(path) as image:
            image.verify()
    except (UnidentifiedImageError, OSError) as error:
        raise IPRegistrationError(f"unreadable reference image: {path}") from error


def _yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def register_ip(
    slug: str,
    display_name: str,
    references: list[Path],
    ip_root: Path,
) -> Path:
    """Create a pending-confirmation person IP package without overwriting data."""
    if not SLUG_PATTERN.fullmatch(slug):
        raise IPRegistrationError(
            "slug must match [a-z0-9][a-z0-9-]{0,62}"
        )
    if not display_name.strip():
        raise IPRegistrationError("display name must not be empty")
    if not references:
        raise IPRegistrationError("at least one reference image is required")

    ip_root = Path(ip_root)
    source_paths = [Path(path) for path in references]
    package = ip_root / slug
    if package.exists():
        raise IPRegistrationError(f"IP package already exists: {package}")

    for source in source_paths:
        _validate_reference(source)

    reference_dir = package / "references"
    reference_dir.mkdir(parents=True)
    relative_references: list[str] = []
    for index, source in enumerate(source_paths, start=1):
        filename = f"reference-{index:02d}{source.suffix.lower()}"
        destination = reference_dir / filename
        shutil.copy2(source, destination)
        relative_references.append(f"references/{filename}")

    profile_lines = [
        f"id: {_yaml_string(slug)}",
        f"display_name: {_yaml_string(display_name)}",
        "status: pending_confirmation",
        "references:",
        *[f"  - {_yaml_string(path)}" for path in relative_references],
        "identity_notes: []",
        "wardrobe_preferences: []",
        "avoid: []",
    ]
    (package / "profile.yaml").write_text(
        "\n".join(profile_lines) + "\n", encoding="utf-8"
    )
    return package


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create a pending-confirmation person IP package from local images."
    )
    parser.add_argument("slug")
    parser.add_argument("display_name")
    parser.add_argument("references", nargs="+", type=Path)
    parser.add_argument(
        "--ip-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "assets" / "ip",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        package = register_ip(
            args.slug,
            args.display_name,
            args.references,
            args.ip_root,
        )
    except (IPRegistrationError, OSError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1

    print(
        json.dumps(
            {"ok": True, "package": str(package.resolve()), "status": "pending_confirmation"},
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
