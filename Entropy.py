#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:36:17 2019

@author: abhrajyotidas
"""

import math
from PIL import Image
imageFile = 'chest-xray.jpg'
print(imageFile)
im = Image.open(imageFile)
rgbHistogram = im.histogram()
print('Snannon Entropy for Red, Green, Blue:')
for rgb in range(1):
     totalPixels = sum(rgbHistogram[rgb * 256 : (rgb + 1) * 256])
     ent = 0.0
     for col in range(rgb * 256, (rgb + 1) * 256):
         freq = float(rgbHistogram[col]) / totalPixels
         if freq > 0:
             ent = ent + freq * math.log(freq, 2)
     ent = -ent
     print(ent)