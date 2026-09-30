import tempfile
import unittest
from pathlib import Path

from PIL import Image

from scripts.register_ip import IPRegistrationError, register_ip


class RegisterIPTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.sources = self.root / "sources"
        self.ip_root = self.root / "assets" / "ip"
        self.sources.mkdir(parents=True)

    def tearDown(self):
        self.temp_dir.cleanup()

    def make_image(self, name: str, image_format: str | None = None) -> Path:
        path = self.sources / name
        Image.new("RGB", (80, 120), "white").save(path, format=image_format)
        return path

    def test_registers_one_image_with_pending_confirmation(self):
        source = self.make_image("portrait.png")

        package = register_ip("my-ip", "我的人物IP", [source], self.ip_root)

        self.assertEqual(package, self.ip_root / "my-ip")
        self.assertTrue((package / "references" / "reference-01.png").is_file())
        profile = (package / "profile.yaml").read_text(encoding="utf-8")
        self.assertIn('id: "my-ip"', profile)
        self.assertIn('display_name: "我的人物IP"', profile)
        self.assertIn("status: pending_confirmation", profile)
        self.assertIn("references/reference-01.png", profile)

    def test_registers_multiple_supported_formats(self):
        first = self.make_image("front.jpg", "JPEG")
        second = self.make_image("side.webp", "WEBP")

        package = register_ip("multi-view", "多视图", [first, second], self.ip_root)

        self.assertTrue((package / "references" / "reference-01.jpg").is_file())
        self.assertTrue((package / "references" / "reference-02.webp").is_file())

    def test_rejects_invalid_and_traversal_slugs_without_writing_outside_root(self):
        source = self.make_image("portrait.png")
        outside = self.ip_root.parent / "escape"

        for slug in ("../escape", "Bad_Name", "含中文", " has-space"):
            with self.subTest(slug=slug):
                with self.assertRaisesRegex(IPRegistrationError, "slug"):
                    register_ip(slug, "人物", [source], self.ip_root)

        self.assertFalse(outside.exists())
        self.assertFalse(self.ip_root.exists())

    def test_rejects_missing_source_before_creating_package(self):
        with self.assertRaisesRegex(IPRegistrationError, "does not exist"):
            register_ip("missing", "人物", [self.sources / "missing.png"], self.ip_root)

        self.assertFalse((self.ip_root / "missing").exists())

    def test_rejects_unsupported_extension_before_creating_package(self):
        source = self.sources / "portrait.gif"
        source.write_bytes(b"GIF89a")

        with self.assertRaisesRegex(IPRegistrationError, "unsupported"):
            register_ip("bad-format", "人物", [source], self.ip_root)

        self.assertFalse((self.ip_root / "bad-format").exists())

    def test_rejects_unreadable_supported_image_before_creating_package(self):
        source = self.sources / "broken.png"
        source.write_bytes(b"not an image")

        with self.assertRaisesRegex(IPRegistrationError, "unreadable"):
            register_ip("broken", "人物", [source], self.ip_root)

        self.assertFalse((self.ip_root / "broken").exists())

    def test_existing_package_is_not_overwritten(self):
        source = self.make_image("portrait.png")
        existing = self.ip_root / "existing"
        existing.mkdir(parents=True)
        marker = existing / "keep.txt"
        marker.write_text("keep", encoding="utf-8")

        with self.assertRaisesRegex(IPRegistrationError, "already exists"):
            register_ip("existing", "人物", [source], self.ip_root)

        self.assertEqual(marker.read_text(encoding="utf-8"), "keep")


if __name__ == "__main__":
    unittest.main()
