import os
import sys
import errno
from PIL import Image
import glob

def main():
    trymakedir("Large")
    trymakedir("Medium")
    trymakedir("Small")

    files = glob.glob("*.png")
    files.extend(glob.glob("*.jpg"))
    files.extend(glob.glob("*.jpeg"))

    for infile in files:
        filename, ext = os.path.splitext(infile)
        generatevariants(filename, ext)


def trymakedir(name):
    if not os.path.exists(name):
        os.mkdir(name)


def generatevariants(filename, ext):
    img = Image.open(filename + ext)

    imgLarge = img.resize((82, 52))
    imgMedium = img.resize((41, 26))
    imgSmall = img.resize((10, 7))

    imgLarge.save(f"Large/{filename}_large{ext}", "PNG")
    imgMedium.save(f"Medium/{filename}_medium{ext}", "PNG")
    imgSmall.save(f"Small/{filename}_small{ext}", "PNG")


main()
