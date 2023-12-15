#!/usr/bin/env python3

from os import mkdir, path
from struct import pack, unpack
from PIL import Image

import sys

IMAGE_HEIGHT = 256
IMAGE_WIDTH = 192
IMAGE_SIZE = (IMAGE_WIDTH * IMAGE_HEIGHT) * 2

def convert_bm(file_path):
    with open(file_path, "rb") as f:
        i = 0
        f.seek(8)
        buf = f.read(IMAGE_SIZE)

        if len(buf) != (IMAGE_SIZE):
            exit("Error: Incorrect image size!")

        rgb = b""

        for j in range(0, (IMAGE_SIZE), 2):
            val, = unpack("<H", buf[j:j+2])
            r = (val & 0x1F) << 3
            g = ((val >> 5) & 0x1F) << 3
            b = ((val >> 10) & 0x1F) << 3
            rgb += pack("BBB", r, g, b)

        im = Image.new("RGB", (IMAGE_HEIGHT, IMAGE_WIDTH))
        im.frombytes(rgb)

        im.save(f"output.bmp")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Converts RAW 16bpp (.bm) file to bitmap.\n")
        print("Usage: python3 bm2bmp.py <input.bm>")
        sys.exit(1)

    file_path = sys.argv[1]
    convert_bm(file_path)
