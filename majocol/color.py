from typing import List, Optional

import numpy as np
from sklearn.cluster import KMeans

from majocol.utils import is_positive_int, rgb2hex


def pick(image_rgb: np.ndarray, count: int = 1) -> Optional[List[str]]:
    """
    Pick major colors from image
    """
    if not is_positive_int(count):
        return None

    image_height = image_rgb.shape[0]
    image_width = image_rgb.shape[1]

    image_size = image_height * image_width
    rgb_ndarray = image_rgb.reshape(image_size, 3)

    cluster = KMeans(n_clusters=count, random_state=0)
    cluster.fit(rgb_ndarray)
    centers_arr = cluster.cluster_centers_.astype(np.uint8, copy=False)

    hex_colors = [rgb2hex(*dec_colors) for dec_colors in centers_arr]

    return hex_colors
