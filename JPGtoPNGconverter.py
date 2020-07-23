import sys
import os
from PIL import Image

# grab first and second argument => Pokedex/ new/

input_folder = sys.argv[1]
output_folder = sys.argv[2]
print(input_folder, output_folder)

# check if new/ exists, if not create it
# hint: use os module

new_path = './new/'
isFile = os.path.exists(new_path)
print(isFile)

if not isFile:
    new_dir = "new"
    os.mkdir(new_dir)

# loop through Pokedex,
# convert images to png
# save to the new folder

for file in os.listdir(input_folder):
    img = Image.open(f'{input_folder}{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
