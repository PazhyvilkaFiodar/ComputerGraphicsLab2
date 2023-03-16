import os
from PIL import Image


def read_images_from_folder(folder: str) -> dict[str, Image.Image]:
    res: dict[str, Image.Image] = dict()
    for filename in os.listdir(folder):
        try:
            image = Image.open(os.path.join(folder, filename))
            res[filename] = image
        except Exception:
            continue

    return res


def get_image_size(image: Image.Image) -> tuple[int, int]:
    return image.size


def get_image_dpi(image: Image.Image) -> tuple[int, int]:
    return image.info.get("dpi", (72, 72))


def get_image_color_depth(image: Image.Image) -> int:
    mode_to_bpp = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32,
                   "YCbCr": 24, "LAB": 24, "HSV": 24, "I": 32, "F": 32}
    return mode_to_bpp[image.mode]


def get_image_compression(image: Image.Image) -> float:
    return image.entropy()
