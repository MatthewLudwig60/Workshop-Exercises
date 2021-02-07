#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:05:53 2021

@author: Matthew
"""

import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import ticker, cm 
# def f1(x, y):
#     array = np.zeros((x, y))
#     for i in range(x):
#         for j in range(y):
#             array[i, j] = np.sin(i) * np.sin(j)
#     return array
# Array = f1(20, 20)

# def f2(x, y, N):
#     array = np.zeros((x, y))
#     for i in range(x):
#         for j in range(y):
#             array[i, j] = np.sin(i) * np.sin(j)
#     x1 = np.linspace(0, x, N)
#     y1 = np.linspace(0, y, N)
#     cs = plt.contourf(x1, y1, array,  
#                   hatches =['-', '/', 
#                             '\\', '//'], 
#                   cmap ='Greens', 
#                   extend ='both', 
#                   alpha = 1)
#     plt.colorbar(cs)
#     plt.show()
# f2(20, 20, 20)

def f3(x, y, N):
    array = np.zeros((N, N)) # N x N matrix
    x1 = np.linspace(0, x, N) 
    y1 = np.linspace(0, y, N)
    for i in range(N):
        for j in range(N):
            array[i, j] = np.sin(x1[i]) * np.sin(y1[j])
    cs = plt.contourf(x1, y1, array,  
                  hatches =['-', '/', 
                            '\\', '//'], 
                  cmap ='Greens', 
                  extend ='both', 
                  alpha = 1)
    plt.colorbar(cs)
    plt.xlabel('sin(x)')
    plt.ylabel('sin(y)')
    plt.show()
f3(40.5, 40, 1000)