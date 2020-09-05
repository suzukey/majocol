import cv2
import numpy as np


def byte_to_cv2_rgb(bytes_image: bytes):
    """
    Convert image from byte to cv2
    """
    bytearr_image = bytearray(bytes_image.read())
    image = np.asarray(bytearr_image, dtype=np.uint8)
    cv2_image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    rgb_image = cv2_bgr_to_rgb(cv2_image)
    return rgb_image


def cv2_bgr_to_rgb(cv2_image):
    """
    Convert color order from BGR to RGB
    """
    rgb_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    return rgb_image
