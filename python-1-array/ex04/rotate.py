import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load, print_info


def ft_transpose(img: list[list]) -> list[list]:
    rows = len(img)
    columns = len(img[0])
    return ([[img[i][j] for i in range(rows)] for j in range(columns)])


def main(path: str):
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
