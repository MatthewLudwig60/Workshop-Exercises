#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:22:37 2021

@author: Matthew
"""

import numpy as np
import matplotlib.pyplot as plt
def f4(x, y):
    return np.sin(x) * np.cos(y)
n = 12
x = np.linspace(0, 1, n)
y = np.linspace(0, 2*np.pi, n)

# data1 = f4(0.2, y)
# plt.plot(y, data1)

data2 = f4(x, y[4])
plt.plot(x, data2)