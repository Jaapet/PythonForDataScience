import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load, print_info


def main(path: str, le: int, to: int, ri: int, bo: int):
    """
    Image Processing Script using NumPy and Matplotlib.

    This script loads an image, crops it based on specified dimensions,
    converts it to grayscale, and displays the result using Matplotlib.

    Functions:
    -----------
    main(path: str, le: int, to: int, ri: int, bo: int)
        - Loads an image from the specified path.
        - Crops the image using left (le), top (to),
          right (ri), and bottom (bo) offsets.
        - Converts the cropped image to grayscale.
        - Displays the grayscale image with specified ticks.

    Parameters:
    -----------
    - path (str): The file path of the image to be processed.
    - le (int): Left crop margin.
    - to (int): Top crop margin.
    - ri (int): Right crop margin.
    - bo (int): Bottom crop margin.
    """
    try:
        img = ft_load(path)
        width, height = img.size
        crop = img.crop((le, to, width - ri, height - bo))  # ltrb
        g_scale = crop.convert('L')
        print_info(np.array(g_scale), "New shape after slicing: ")

        fig, ax = plt.subplots()
        ax.imshow(np.array(g_scale), cmap='gray')
        ax.set_xticks(np.arange(0, np.array(g_scale).shape[1], 50))
        ax.set_yticks(np.arange(0, np.array(g_scale).shape[0], 50))
        ax.tick_params(axis='both', which='both', direction='out')
        plt.show()

    except Exception as e:
        print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main("animal.jpeg", 100, 300, 500, 100)
