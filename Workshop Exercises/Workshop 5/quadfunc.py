#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:28:25 2020

@author: Matthew
"""
import matplotlib.pyplot as plt

def quadfunc(a, b, x):
    value = a*x + b*x**2
    return value
print(quadfunc(1,2,3))
X = []
Quadfunc = []
for i in range(0, 11):
    X.append(i)
    Quadfunc.append(quadfunc(1, 2, i))
plt.figure()
plt.plot(X, Quadfunc, 'r+')
