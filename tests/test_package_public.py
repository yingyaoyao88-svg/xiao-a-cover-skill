import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from package_public import FILES, audit_public


class PublicPackageTests(unittest.TestCase):
    def make_fixture(self, root):
        for name in FILES:
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)

    def test_public_source_contains_required_reviewed_assets(self):
        self.assertTrue({ROOT / name for name in FILES}.issubset(set(audit_public(ROOT))))

    def test_rejects_accidentally_added_person_photo(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.make_fixture(root)
            (root / "private-turnaround.png").write_bytes(b"private image")
            with self.assertRaisesRegex(ValueError, "Unlisted file"):
                audit_public(root)

    def test_rejects_modified_image_at_an_approved_showcase_path(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.make_fixture(root)
            (root / "docs/showcase/codex-touch-screen.png").write_bytes(b"unapproved replacement")
            with self.assertRaisesRegex(ValueError, "approved hash"):
                audit_public(root)


if __name__ == "__main__":
    unittest.main()
