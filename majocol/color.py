from sklearn.cluster import KMeans

from majocol.utils import is_positive_int
from majocol.types import HexRgb


# TODO Returns a list of HexRgb
def pick(rgb_image, count: int = 1) -> HexRgb:
    """
    Pick major colors from image
    """
    if not is_positive_int(count):
        return None

    try:
        image_shape = rgb_image.shape[0] * rgb_image.shape[1]
        img = rgb_image.reshape(image_shape, 3)
    except BaseException:
        return None

    cluster = KMeans(n_clusters=count)
    cluster.fit(X=img)

    centers_arr = cluster.cluster_centers_.astype(int, copy=False)
    for rgb_arr in centers_arr:
        color_hex = '%02x%02x%02x' % tuple(rgb_arr)

    return color_hex
