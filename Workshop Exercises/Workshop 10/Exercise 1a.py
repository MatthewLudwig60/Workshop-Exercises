#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:13:44 2021

@author: Matthew
"""

import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return np.exp(-x) * np.cos(2*np.pi*x)
def f2(x):
    return np.cos(x)
def f3(x):
    return np.sin(x)
def addfunctions(fa, fb, x):
    return fb(x) + fa(x)
n = 12
x = np.linspace(0, 1, n)
# print(f'Add functions {addfunctions(f1, f2, x[4])} {f1(x[4]) + f2(x[4])}')
# print(x[4])
# print(x)
# print(f2(x[4])) 
# print(f2(x))
data = addfunctions(f1, f2, x)
plt.plot(x, data)