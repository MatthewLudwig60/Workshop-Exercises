#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:07:01 2021

@author: Matthew
"""

import numpy as np
nx = 10
ny = 5
nz = 3

mult_array = np.zeros((nx, ny, nz))


for i in range(nx):
    for j in range(ny):
        for k in range(nz):
            if i == j:
                mult_array[i, j, k] = 1
            elif j == k:
                mult_array[i, j, k] = 1
            elif i == k:
                mult_array[i, j, k] = 1

for i in range(nx):
    print(mult_array[i][1])
            
    