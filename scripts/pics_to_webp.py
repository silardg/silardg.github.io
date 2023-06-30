# import required module
import os
from PIL import Image
import PIL
import os
import glob
from pathlib import Path
directory = '../pics'
 
pics = Path("../pics")
all_files = pics.rglob("*")

for current_file in all_files:
    if os.path.isfile(current_file):
        if current_file.suffix == '.webp':
            print("Deleting" + str(current_file))
            Path.unlink(current_file)

all_files = pics.rglob("*")

for current_file in all_files:
    if os.path.isfile(current_file):
        if current_file.suffix == '.png':
            print("Converting" + str(current_file))
            image = Image.open(str(current_file))
            image = image.convert('RGBA')
            new_filename = Path(current_file).with_suffix(".webp")
            image.save(new_filename, 'webp')
