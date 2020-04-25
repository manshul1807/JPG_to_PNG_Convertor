import sys
import os
from PIL import Image

# grab first and second argument
current_folder = sys.argv[1:][0]
converted_folder = sys.argv[1:][1]

# check is new folder exists, if not create
if not os.path.isdir(converted_folder):
    os.mkdir(converted_folder)

# loop through pokedex

for filename in os.listdir(current_folder):
    image = Image.open(os.path.join(current_folder, filename))
    converted_image = image.copy()
    original_name = os.path.basename(filename)
    converted_name = original_name[:-4]+'.png'
    com_converted_name = os.path.join(converted_folder, converted_name)
    converted_image.save(com_converted_name, 'png')
