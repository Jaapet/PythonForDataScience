import numpy as np
from load_image import ft_load, print_info


def main(path: str, le: int, to: int, ri: int, bo: int):
    try:
        img = ft_load(path)
        width, height = img.size
        crop = img.crop((le, to, width - ri, height - bo))  # ltrb
        g_scale = crop.convert('L')
        print_info(np.array(g_scale), "New shape after slicing: ")
        g_scale.show()
    except Exception as e:
        print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main("animal.jpeg", 100, 300, 500, 100)
