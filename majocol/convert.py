import io

import numpy as np
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
