import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps


def ft_display(img: Image) -> None:
    fig, ax = plt.subplots()
    ax.imshow(np.array(img), cmap='gray')
    ax.set_xticks(np.arange(0, np.array(img).shape[1], 50))
    ax.set_yticks(np.arange(0, np.array(img).shape[0], 50))
    ax.tick_params(axis='both', which='both', direction='out')
    plt.show()


def ft_invert(array) -> np.array:
    try:
        img = Image.fromarray(np.array(array, dtype=np.uint8))
        mod = ImageOps.invert(img)
        ft_display(mod)
        return np.array(mod)
    except Exception as e:
        print(f"{Exception.__name__}: {e}")


def ft_red(array) -> np.array:
    try:
        img = Image.fromarray(np.array(array, dtype=np.uint8))
        r, g, b = img.split()
        mod = Image.merge("RGB", (r, Image.new("L", g.size, 0),
                                  Image.new("L", b.size, 0)))
        ft_display(mod)
        return np.array(mod)
    except Exception as e:
        print(f"{Exception.__name__}: {e}")


def ft_green(array) -> np.array:
    try:
        img = Image.fromarray(np.array(array, dtype=np.uint8))
        r, g, b = img.split()
        mod = Image.merge("RGB", (Image.new("L", r.size, 0), g,
                                  Image.new("L", b.size, 0)))
        ft_display(mod)
        return np.array(mod)
    except Exception as e:
        print(f"{Exception.__name__}: {e}")


def ft_blue(array) -> np.array:
    try:
        img = Image.fromarray(np.array(array, dtype=np.uint8))
        r, g, b = img.split()
        mod = Image.merge("RGB", (Image.new("L", r.size, 0),
                                  Image.new("L", g.size, 0), b))
        ft_display(mod)
        return np.array(mod)
    except Exception as e:
        print(f"{Exception.__name__}: {e}")


def ft_grey(array) -> np.array:
    try:
        img = Image.fromarray(np.array(array, dtype=np.uint8))
        mod = img.convert('L')
        ft_display(mod)
        return np.array(mod)
    except Exception as e:
        print(f"{Exception.__name__}: {e}")
