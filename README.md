<p align="center">
  <img width="420px" src="https://raw.githubusercontent.com/suzukey/majocol/main/docs/img/majocol.png" alt='majocol'>
</p>

<p align="center">
  <em>Pick major colors from image</em>
</p>

<p align="center">
  <a href="https://github.com/suzukey/majocol/actions?query=workflow%3ATest" target="_blank">
    <img src="https://github.com/suzukey/majocol/workflows/Test/badge.svg" alt="Test">
  </a>

  <a href="https://codecov.io/gh/suzukey/majocol" target="_blank">
    <img src="https://img.shields.io/codecov/c/gh/suzukey/majocol" alt="Coverage">
  </a>

  <a href="https://pypi.org/project/majocol/" target="_blank">
    <img src="https://img.shields.io/pypi/v/majocol?color=blue" alt="Package version">
  </a>
</p>

---

**Documentation**:

**Demo**:

---

# MajoCol

## Requirements

Python 3.6+

## Installation

```shell
$ pip3 install majocol
```

## Example

```python
from majocol import color, convert

# Using Pillow (Open local image)
from PIL import Image

image = Image.open(<IMAGE_PATH>)
image_ndarr = convert.pillow_to_rgb_ndarr(image)
colors = color.pick(image_ndarr, 3)


# Using opencv-python (Open local image)
import cv2

image = cv2.imread(<IMAGE_PATH>)
image_ndarr = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
colors = color.pick(image_ndarr, 3)


# Using requests (Fetch web image)
import requests

resp = requests.get(<IMAGE_URL>)
image_ndarr = convert.byte_to_rgb_ndarr(resp.content)
colors = color.pick(image_ndarr, 3)
```

<p align="center">&mdash; 🪄 &mdash;</p>

<p align="center">
  <i>MajoCol is licensed under the terms of the <a href="https://github.com/suzukey/majocol/blob/main/LICENSE">MIT license</a>.</i>
</p>
