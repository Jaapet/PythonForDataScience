import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    try:
        img = Image.open(path)
        img_arr = np.array(img.convert('RGB'))
        print(f"The shape of image is: {img_arr.shape}")
        return img_arr
    except Exception as e:
        print(f"{Exception.__name__}: {e}")
        print("Failed to load the image")
        return []
