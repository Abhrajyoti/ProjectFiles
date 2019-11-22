#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 09:29:02 2019

@author: abhrajyotidas
"""

from PIL import Image
import re

triplet = r'\((\d+), (\d+), (\d+)\)' # regex pattern

image = []
with open('check_conv.txt') as fp:
    for line in fp:
        image.append([(int(x), int(y), int(z)) for x, y, z in re.findall(triplet, line)])
width, height = len(image[0]), len(image)
data = sum(image, []) # ugly hack to flatten the image

im = Image.new('RGB', (width, height))
im.putdata(data)
im.save('image.png')