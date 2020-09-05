from typing import Any


def is_positive_int(target: Any) -> bool:
    """
    Whether `target` is positive integer or not
    """
    return isinstance(target, int) and target > 0
