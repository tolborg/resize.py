#!/usr/bin/env python

import os
import shutil
import glob
from PIL import Image

current_dir = os.getcwd()
large_dir = current_dir + "/large"
small_dir = current_dir + "/small"

image_paths = glob.glob(large_dir + "/*.PNG")

shutil.rmtree(small_dir, ignore_errors=True)
os.mkdir(small_dir)

for image_path in image_paths:
  filename = os.path.basename(image_path)
  img = Image.open(image_path)
  new_size = img.size[0]/2, img.size[1]/2
  img.thumbnail(new_size, Image.ANTIALIAS)
  img.save(small_dir + "/" + filename)
