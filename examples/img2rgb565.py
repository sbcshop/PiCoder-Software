# Set the encoding to UTF-8
# This is important when working with non-ASCII characters in the code or input files
# as it ensures that the interpreter can correctly decode them.
# Without this, the program may crash with a UnicodeDecodeError.
# For more information: https://docs.python.org/3/howto/unicode.html
# -*- coding: utf-8 -*-

# Import necessary modules
from PIL import Image
from struct import pack
from os import path
import sys


def error(msg):
    """Display error and exit."""
    print (msg)
    sys.exit(-1)


def write_bin(f, pixel_list):
    """Save image in RGB565 format."""
    # Convert each pixel's RGB values to RGB565 format
    for pix in pixel_list:
        r = (pix[0] >> 3) & 0x1F
        g = (pix[1] >> 2) & 0x3F
        b = (pix[2] >> 3) & 0x1F
        # Write the pixel data to the output file in big-endian byte order
        f.write(pack('>H', (r << 11) + (g << 5) + b))


if __name__ == '__main__':
    # Get the input filename from the command-line arguments
    args = sys.argv
    # Check that only one argument was passed (the input filename)
    if len(args) != 2:
        error('Please specify input file: ./img2rgb565.py testing.jpg')
    # Get the input filename and check that it exists
    in_path = args[1]
    if not path.exists(in_path):
        error('File Not Found: ' + in_path)

    # Set the output filename to the input filename with .raw extension
    filename, ext = path.splitext(in_path)
    out_path = filename + '.raw'
    # Open the input image and convert it to RGB mode
    img = Image.open(in_path).convert('RGB')
    # Get the RGB values for each pixel in the image and store them in a list
    pixels = list(img.getdata())
    # Open the output file and write the RGB565 pixel data to it
    with open(out_path, 'wb') as f:
        write_bin(f, pixels)
    # Print a message indicating that the output file was saved
    print('Saved: ' + out_path)