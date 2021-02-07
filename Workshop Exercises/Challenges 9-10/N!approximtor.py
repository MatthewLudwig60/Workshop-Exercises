#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:41:19 2020

@author: Matthew
"""
import numpy as np
import matplotlib.pyplot as plt
def factorial(N):
    answer = 1
    for i in range(2, (N+1)):
        answer = answer * i
    return answer
approxlogN = []
exactlogN = []
index = []
error = []
for i in range(2, 160):
    approxlog = i*np.log10(i)-i
    approxlogN.append(approxlog)
    exactlog = np.log10(float(factorial(i)))
    exactlogN.append(exactlog)
    index.append(i)
    error.append(abs(approxlog - exactlog))
plt.figure()
plt.plot(index, exactlogN)
plt.plot(index, approxlogN)
plt.plot(index, error)

