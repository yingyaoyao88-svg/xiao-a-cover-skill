"""Package the public skill, allowing only four explicitly approved showcase images."""

import argparse
import hashlib
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SHOWCASE_SHA256 = {
    "docs/showcase/codex-touch-screen.png": "60217e81970900c581fc3d034bf732d4d69705d7c04d27c2af4fd237f41ca3af",
    "docs/showcase/codex-result-in-hand.png": "f8fba937ac937da3edcfe6d4424638d98b922a065542fc554a346f61c118ce91",
    "docs/showcase/codex-command-desk.png": "c06697e00e5d74298da36f74b45fa330d8b3d499f654a56422f89fce6adb4166",
    "docs/showcase/codex-cross-screen-drag.png": "c1ffb71cc83336b8114d51d562f8c8805960054a5495cb75a05ccaee0f85fc75",
}
FILES = (
    "SKILL.md", "README.md", "使用说明.md", ".gitignore", "requirements.txt",
    "references/onboarding.md", "references/styles.md", "references/prompt-patterns.md",
    "scripts/finalize_cover.py", "scripts/package_public.py",
    "tests/test_finalize_cover.py", "tests/test_package_public.py",
    "docs/showcase/README.md", *SHOWCASE_SHA256,
)
REPOSITORY_FILES = {
    "LICENSE", ".python-version", "pyproject.toml", ".github/workflows/ci.yml",
    "agents/openai.yaml", "tests/__init__.py",
}


def audit_public(root):
    root = Path(root).resolve()
    found = set()
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in {".git", "__pycache__", ".pytest_cache", ".ruff_cache"} for part in relative.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"Symlinks are not permitted in the public package: {relative}")
        if not path.is_file():
            continue
        name = relative.as_posix()
        if name not in FILES and name not in REPOSITORY_FILES:
            raise ValueError(f"Unlisted file must be reviewed before publishing: {relative}")
        found.add(name)
        if name in SHOWCASE_SHA256:
            if hashlib.sha256(path.read_bytes()).hexdigest() != SHOWCASE_SHA256[name]:
                raise ValueError(f"Showcase image does not match its approved hash: {relative}")
            continue
        content = path.read_text(encoding="utf-8")
        if path.suffix == ".svg":
            lowered = content.lower()
            if any(token in lowered for token in ("<image", "data:", "foreignobject", "<script")):
                raise ValueError(f"Public SVG must contain only simple vector artwork: {relative}")
    missing = set(FILES) - found
    if missing:
        raise ValueError(f"Missing public files: {sorted(missing)}")
    return [root / name for name in (*FILES, *sorted(found.intersection(REPOSITORY_FILES)))]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    files = audit_public(ROOT)
    destination = args.destination.resolve()
    if destination.is_relative_to(ROOT):
        raise ValueError("Keep generated archives outside the public source folder")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, "xiao-a-cover/" + path.relative_to(ROOT).as_posix())
    print(f"Public package verified: {len(files)} reviewed files, four approved showcases; {destination}")


if __name__ == "__main__":
    main()
