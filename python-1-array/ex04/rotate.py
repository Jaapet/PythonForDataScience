import numpy as np
from PIL import Image
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
        Image.fromarray(np.array(get_rotated_idiot, dtype=np.uint8)).show()
    except Exception as e:
        print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main("animal.jpeg")
