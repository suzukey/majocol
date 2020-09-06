import numpy as np
from sklearn.cluster import KMeans

from majocol.utils import is_positive_int, rgb2hex
from majocol.types import HexRgbList


def pick(image_ndarray, count: int = 1) -> HexRgbList:
    """
    Pick major colors from image
    """
    if not is_positive_int(count):
        return None

    image_height = image_ndarray.shape[0]
    image_width = image_ndarray.shape[1]

    image_size = image_height * image_width
    rgb_ndarray = image_ndarray.reshape(image_size, 3)

    cluster = KMeans(n_clusters=count)
    cluster.fit(X=rgb_ndarray)
    centers_arr = cluster.cluster_centers_.astype(np.uint8, copy=False)

    hex_colors = [rgb2hex(*dec_colors) for dec_colors in centers_arr]
    return hex_colors
