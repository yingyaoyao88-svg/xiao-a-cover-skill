"""Validate a native 3:4 cover and resize its whole canvas to 1080x1440."""

import argparse
import json
from pathlib import Path

from PIL import Image, ImageOps


TARGET_SIZE = (1080, 1440)
TARGET_RATIO = TARGET_SIZE[0] / TARGET_SIZE[1]


def finalize_cover(source, destination, tolerance=0.005, overwrite=False):
    source = Path(source)
    destination = Path(destination)
    if destination.exists() and not overwrite:
        raise FileExistsError(f"Destination already exists: {destination}")

    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened)
        width, height = image.size
        ratio_error = abs(width / height - TARGET_RATIO)
        if ratio_error > tolerance:
            raise ValueError(
                f"Source is not close to 3:4: {width}x{height} "
                f"(ratio error {ratio_error:.6f}); regenerate, do not crop"
            )
        output = image.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
        if output.mode not in ("RGB", "RGBA"):
            output = output.convert("RGBA" if "A" in output.getbands() else "RGB")
        destination.parent.mkdir(parents=True, exist_ok=True)
        output.save(destination, format="PNG")

    return {
        "ok": True,
        "source": str(source.resolve()),
        "destination": str(destination.resolve()),
        "source_size": [width, height],
        "final_size": list(TARGET_SIZE),
        "ratio_error": ratio_error,
        "cropped": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("destination")
    parser.add_argument("--tolerance", type=float, default=0.005)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    result = finalize_cover(
        args.source, args.destination, tolerance=args.tolerance, overwrite=args.overwrite
    )
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
