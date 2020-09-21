import io

import numpy as np
from fitrate import scale_down
from PIL import Image


def byte_to_rgb_ndarr(image_bytes: bytes) -> np.ndarray:
    """
    Convert image from `byte` to `ndarray(rgb)`
    """
    bytes_load = io.BytesIO(image_bytes)
    image_pillow = Image.open(bytes_load)
    image_ndarray = pillow_to_rgb_ndarr(image_pillow)

    return image_ndarray


def pillow_to_rgb_ndarr(image_pillow: Image) -> np.ndarray:
    """
    Convert image from `Pillow` to `ndarray(rgb)`
    """
    image_ndarray = np.array(image_pillow.convert("RGB"))

    return image_ndarray


def resize_pixel(image: np.ndarray, max_pixel: int = 60000) -> np.ndarray:
    """
    Make the image smaller to reduce the time it takes to run K-means
    """
    image_pil = Image.fromarray(image)

    origin_width = image_pil[0]
    origin_height = image_pil[1]

    rescale = scale_down((origin_width, origin_height), max_pixel)
    image_pil.resize(rescale)

    image_ndarray = pillow_to_rgb_ndarr(image_pil)

    return image_ndarray
