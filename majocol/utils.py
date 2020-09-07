from functools import lru_cache
from typing import Any

from majocol.types import Uint8


def is_positive_int(target: Any) -> bool:
    """
    Whether `target` is positive integer or not
    """
    return isinstance(target, int) and target > 0


@lru_cache(maxsize=None)
def rgb2hex(r: Uint8, g: Uint8, b: Uint8) -> str:
    """
    Convert RGB color from decimal to hexadecimal
    """
    return '#%02x%02x%02x' % (r, g, b)
