import pytest

from majocol.utils import is_positive_int, rgb2hex


@pytest.mark.parametrize(
    "target,expected_response",
    [
        (1, True),
        (100, True),
        (0, False),
        ('1', False),
        (3.14, False),
    ],
)
def test_is_positive_int(target, expected_response):
    assert is_positive_int(target) is expected_response


@pytest.mark.parametrize(
    "r,g,b,expected_response",
    [
        (255, 255, 255, '#ffffff'),
        (0, 0, 0, '#000000'),
        (29, 80, 162, '#1d50a2'),
    ],
)
def test_rgb2hex(r, g, b, expected_response):
    assert rgb2hex(r, g, b) == expected_response
