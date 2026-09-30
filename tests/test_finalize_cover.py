import tempfile
import unittest
from pathlib import Path

from PIL import Image

from scripts.finalize_cover import CoverFinalizationError, finalize_cover


class FinalizeCoverTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def make_image(self, relative_path: str, size: tuple[int, int]) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        Image.new("RGB", size, "white").save(path)
        return path

    def test_exact_three_by_four_is_resized_without_crop(self):
        source = self.make_image("source.png", (768, 1024))
        destination = self.root / "cover.png"

        result = finalize_cover(source, destination)

        with Image.open(destination) as output:
            self.assertEqual(output.size, (1080, 1440))
        self.assertEqual(result["source_size"], [768, 1024])
        self.assertEqual(result["final_size"], [1080, 1440])
        self.assertFalse(result["cropped"])

    def test_small_ratio_error_within_tolerance_is_accepted(self):
        source = self.make_image("near.png", (750, 1001))
        destination = self.root / "near-cover.png"

        result = finalize_cover(source, destination)

        self.assertTrue(destination.exists())
        self.assertLessEqual(result["ratio_error"], 0.002)

    def test_non_three_by_four_image_is_rejected_without_output(self):
        source = self.make_image("wide.png", (1600, 900))
        destination = self.root / "must-not-exist.png"

        with self.assertRaisesRegex(CoverFinalizationError, "3:4"):
            finalize_cover(source, destination)

        self.assertFalse(destination.exists())

    def test_unicode_and_space_paths_are_supported(self):
        source = self.make_image("中文 目录/原图.png", (1080, 1440))
        destination = self.root / "输出 目录" / "封面.png"

        finalize_cover(source, destination)

        self.assertTrue(destination.exists())
        with Image.open(destination) as output:
            self.assertEqual(output.size, (1080, 1440))

    def test_existing_destination_is_not_overwritten_by_default(self):
        source = self.make_image("source.png", (768, 1024))
        destination = self.make_image("existing.png", (20, 20))
        before = destination.read_bytes()

        with self.assertRaisesRegex(CoverFinalizationError, "already exists"):
            finalize_cover(source, destination)

        self.assertEqual(destination.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
