from functools import lru_cache
from typing import Any


def is_positive_int(target: Any) -> bool:
    """
    Whether `target` is positive integer or not
    """
    return isinstance(target, int) and target > 0


@lru_cache(maxsize=None)
def rgb2hex(r: int, g: int, b: int) -> str:
    """
    Convert RGB color from decimal to hexadecimal
    """
    return '#%02x%02x%02x' % (r, g, b)
