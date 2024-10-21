import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load, print_info


def ft_transpose(img: list[list]) -> list[list]:
    """
    Transpose a 2D list (matrix).
    Args:
        img (list[list]): A 2D list representing an image.
    Returns:
        list[list]: A new 2D list that is the transpose of the input image.
    """
    rows = len(img)
    columns = len(img[0])
    return ([[img[i][j] for i in range(rows)] for j in range(columns)])


def main(path: str):
    """
    Main function to load an image, crop it, convert it to grayscale,
    transpose the image, and display the result.

    Args:
        path (str): The file path of the image to be processed.

    Raises:
        Exception: Any exception that occurs during
        image processing will be printed.
    """
    try:
        img = ft_load(path)
        crop = img.crop((500, 100, 900, 500))  # ltrb
        g_scale = crop.convert('L')
        get_rotated_idiot = ft_transpose(np.array(g_scale))
        print_info(np.array(get_rotated_idiot), "New shape after Transpose: ")

        fig, ax = plt.subplots()
        ax.imshow(np.array(get_rotated_idiot, dtype=np.uint8), cmap='gray')
        ax.set_xticks(np.arange(0, np.array(get_rotated_idiot,
                                            dtype=np.uint8).shape[1], 50))
        ax.set_yticks(np.arange(0, np.array(get_rotated_idiot,
                                            dtype=np.uint8).shape[0], 50))
        ax.tick_params(axis='both', which='both', direction='out')
        plt.show()

    except Exception as e:
        print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main("animal.jpeg")
