#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:18:45 2019

@author: abhrajyotidas
"""
from PIL import Image
from PIL import ImageChops
import math

def rmsdiff_2011(im1, im2):
    "Calculate the root-mean-square difference between two images"
    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()
    sq = (value*(idx**2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares/float(im1.size[0] * im1.size[1]))
    return rms

def main():
    filename1= "chest-xray.jpg"
    filename2= "chest-xary-cipher.jpg"
    im1 = Image.open(filename1)
#    im1 = intImage(im1)
#    print(im1)
    im2 = Image.open(filename2)
    rms = rmsdiff_2011(im1,im2)
    print(rms)
    
def intImage(image):
    im = Image.open(image)  # Can be many different formats.
    pix = im.load()
    image_size=im.size()
    image_matrix = []
    for width in range(int(image_size[0])):
        row = []
        for height in range(int(image_size[1])):
            try:
                row.append(pix[width,height][0])
            except:
                row=[pix[width,height][0]]
        try:
            image_matrix.append(row)
        except:
            image_matrix = [row]
    return image_matrix

if __name__ == "__main__":
    main()