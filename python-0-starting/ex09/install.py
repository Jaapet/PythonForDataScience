import os

os.system("python3.10 setup.py sdist bdist_wheel")
os.system("pip install ./dist/ft_package-0.0.1.tar.gz")
