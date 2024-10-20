import numpy as np
from PIL import Image


def print_info(img: np.array, s: str) -> None:
    if len(img.shape) < 3:
        img = img.reshape(img.shape[0], img.shape[1], 1)
    print(f"{s}{img.shape}")
    print(img)


def ft_load(path: str) -> Image:
    try:
        img = Image.open(path)
        img_arr = np.array(img.convert('RGB'))
        print_info(img_arr, "The shape of image is: ")
        return img
    except Exception as e:
        print(f"{Exception.__name__}: {e}")
        print("Failed to load the image")
        return []
