import time
import board
import os
import displayio
import adafruit_imageload
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.circle import Circle

# Function to load and append an image to the display group
def load_and_append_image(display_group, image_path):
    with open(image_path, "rb") as image_file:
        image, image_palette = adafruit_imageload.load(image_file)
        image_tilegrid = displayio.TileGrid(image, pixel_shader=image_palette, x=0, y=0)
        display_group.pop()  # Remove the previous image
        display_group.append(image_tilegrid)  # Add the next image

# Set the folder containing your bitmap images
image_folder = "Eyes_Expressions/Love/"  # Replace with the actual folder path

# Create display group
display = board.DISPLAY

# Create a black background fill
bg_bitmap = displayio.Bitmap(display.width, display.height, 1)
bg_palette = displayio.Palette(1)
bg_palette[0] = 0x000000  # Black background
bg_sprite = displayio.TileGrid(bg_bitmap, pixel_shader=bg_palette, x=0, y=0)

# Initialize the display group with the background
splash = displayio.Group()
splash.append(bg_sprite)
display.show(splash)

# Get a list of all bitmap files in the image folder
image_files = [image_folder + f for f in os.listdir(image_folder) if f.endswith(".bmp")]
image_files.sort()  # Sort the image files to ensure they are displayed in order

# Set the duration to display each image (in seconds)
image_duration = 0

while True:
    for image_path in image_files:
        load_and_append_image(splash, image_path)
        time.sleep(image_duration)
