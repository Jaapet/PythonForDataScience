import numpy as np
from PIL import Image


def print_info(img: np.array, s: str) -> None:
    """
    Prints the shape and content of an image array.

    Parameters:
    - img (np.array): The image as a NumPy array.
    - s (str): A string prefix to display before the shape.
    """
    if len(img.shape) < 3:
        img = img.reshape(img.shape[0], img.shape[1], 1)
    print(f"{s}{img.shape}")
    print(img)


def ft_load(path: str) -> Image:
    """
    Loads an image from a specified file path, converts it to RGB,
    and prints its shape and content.

    Parameters:
    - path (str): The file path to the image.

    Returns:
    - Image: The loaded image in PIL format.

    Raises:
    - Exception: If the image cannot be loaded.
    """
    try:
        img = Image.open(path)
        img_arr = np.array(img.convert('RGB'))
        print_info(img_arr, "The shape of image is: ")
        return img
    except Exception as e:
        print(f"{Exception.__name__}: {e}")
        print("Failed to load the image")
        exit()
