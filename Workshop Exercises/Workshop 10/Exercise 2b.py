#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:32:49 2021

@author: Matthew
"""
import numpy as np
import matplotlib.pyplot as plt
# def f1(x, y):
#     return x * (y**2) * np.pi
# datapoints = np.ones((5, 3))
# for i in range(5):
#     for j in range(3):
#         datapoints[i, j] = f1(i, j)
# print(datapoints)

def f1(x, y):
    return x * (y**2) * np.pi
x = np.linspace(0, 4, 5)
y = np.linspace(0, 2, 3)
datapoints = np.ones((len(x), len(y)))
for i in range(len(x)):
    for j in range(len(y)):
        datapoints[i, j] = f1(i, j)
# datapoints1 = f1(3, y)
# plt.plot(y, datapoints1)
datapoints2 = f1(x, 1)
plt.plot(x, datapoints2)