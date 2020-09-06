import io

import numpy as np
from PIL import Image


def byte_to_rgb_ndarr(image_bytes: bytes):
    """
    Convert image from `byte` to `ndarray(rgb)`
    """
    bytes_load = io.BytesIO(image_bytes)
    image_pillow = Image.open(bytes_load)
    image_ndarray = pillow_to_rgb_ndarr(image_pillow)

    return image_ndarray


def pillow_to_rgb_ndarr(image_pillow):
    """
    Convert image from `Pillow` to `ndarray(rgb)`
    """
    image_ndarray = np.array(image_pillow.convert('RGB'))

    return image_ndarray


def cv2_to_rgb_ndarr(image_cv2):
    """
    Convert color order from BGR to RGB

    Requirements: `cv2(opencv-python)`
    """
    import cv2

    image_ndarray = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)

    return image_ndarray
