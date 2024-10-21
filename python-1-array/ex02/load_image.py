import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    Load an image from the specified file path
    and convert it to an RGB NumPy array.

    Parameters:
    - path (str): The file path to the image.

    Returns:
    - np.array: A NumPy array representation of the RGB image.
                Returns an empty list if the image cannot be loaded.

    Raises:
    - Exception: Catches any exceptions during the
    image loading process and prints an error message.
    """
    try:
        img = Image.open(path)
        img_arr = np.array(img.convert('RGB'))
        print(f"The shape of image is: {img_arr.shape}")
        return img_arr
    except Exception as e:
        print(f"{Exception.__name__}: {e}")
        print("Failed to load the image")
        return []
