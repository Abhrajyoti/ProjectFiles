#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:02:40 2019

@author: abhrajyotidas
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

# read image
im = cv2.imread('13.png')
# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
# calculate histogram
counts, bins = np.histogram(vals, range(257))
# plot histogram centered on values 0..255
plt.bar(bins[:-1] -1, counts, width=1, edgecolor='none')
plt.xlim([-2, 255.5])
plt.show()