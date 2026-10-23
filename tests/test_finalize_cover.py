import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from finalize_cover import finalize_cover


class FinalizeCoverTests(unittest.TestCase):
    def test_resizes_whole_native_three_by_four_image(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source.png"
            target = Path(tmp) / "cover.png"
            image = Image.new("RGB", (1086, 1448), "white")
            draw = ImageDraw.Draw(image)
            draw.rectangle((0, 0, 31, 31), fill=(255, 0, 0))
            draw.rectangle((1054, 1416, 1085, 1447), fill=(0, 0, 255))
            image.save(source)

            result = finalize_cover(source, target)

            with Image.open(target) as output:
                self.assertEqual(output.size, (1080, 1440))
                self.assertEqual(output.getpixel((0, 0)), (255, 0, 0))
                self.assertEqual(output.getpixel((1079, 1439)), (0, 0, 255))
            self.assertFalse(result["cropped"])

    def test_rejects_wrong_aspect_ratio(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source.png"
            target = Path(tmp) / "cover.png"
            Image.new("RGB", (1024, 1536), "white").save(source)

            with self.assertRaises(ValueError):
                finalize_cover(source, target)
            self.assertFalse(target.exists())

    def test_does_not_overwrite_without_opt_in(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source.png"
            target = Path(tmp) / "cover.png"
            Image.new("RGB", (1086, 1448), "white").save(source)
            target.write_bytes(b"existing")

            with self.assertRaises(FileExistsError):
                finalize_cover(source, target)
            self.assertEqual(target.read_bytes(), b"existing")


if __name__ == "__main__":
    unittest.main()
