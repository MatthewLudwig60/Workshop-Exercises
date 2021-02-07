#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:32:06 2020

@author: Matthew
"""

import numpy as np
import pylab as plt
def rectint(a, b, N, func):
    x = np.linspace(a, b, N)
    h = x[1] - x[0]
    integral = 0
    for k in range(N):
        integral += func(x[k])
    integral = integral * h
    if func == func1:
        integralerror = abs(0.550935173739280 - integral)
    else:
        integralerror = abs((1/(4+16*(np.pi)**2))*(1-np.exp(-4)) - integral)
    return integralerror
def trapint(a, b, N, func):
    x = np.linspace(a, b, N) #Generates N equally spaced values from a to b
    h = x[1] - x[0] #strip width = 2nd x value - 1st x value
    integral = 0
    for k in range(1, N-1):
        integral += func(x[k]) 
    integral += 0.5*(func(x[0])+func(x[-1]))
    integral = integral * h
    if func == func1:
        integralerror = abs(0.550935173739280 - integral)
    else:
        integralerror = abs((1/(4+16*(np.pi)**2))*(1-np.exp(-4)) - integral)
    return integralerror 
def func1(x):
    return np.sin(np.exp(x))
def func2(x):
    return np.cos(8*np.pi*x)*np.exp(-4*x)
NValues = np.array([6, 10, 15, 20, 100])
#rectintvalues = np.zeros((len(NValues), 2)) 
#trapintvalues = np.zeros((len(NValues), 2)) to use multidimensional arrays
rectintvalues1 = np.zeros((len(NValues)))
rectintvalues2 = np.zeros((len(NValues)))
trapintvalues1 = np.zeros((len(NValues)))
trapintvalues2 = np.zeros((len(NValues)))
                          
for i in range(len(NValues)):
    #rectintvalues[i][0] = (rectint(0, 2, NValues[i], func1))
    #rectintvalues[i][1] = (rectint(0, 1, NValues[i], func2))
    #trapintvalues[i][0] = (trapint(0, 2, NValues[i], func1))
    #trapintvalues[i][1] = (trapint(0, 1, NValues[i], func2)) to use multidimensional arrays
    rectintvalues1[i] = (rectint(0, 2, NValues[i], func1))
    rectintvalues2[i] = (rectint(0, 1, NValues[i], func2))
    trapintvalues1[i] = (trapint(0, 2, NValues[i], func1))
    trapintvalues2[i] = (trapint(0, 2, NValues[i], func2))


plt.figure()
plt.plot(NValues, rectintvalues1, 'r--', label = 'Error in func1 with rect')
plt.plot(NValues, trapintvalues1, 'g--', label = 'Error in func1 with trap')
plt.plot(NValues, rectintvalues2, 'b--', label = 'Error in func2 with rect')
plt.plot(NValues, trapintvalues2, 'k--', label = 'Error in func2 with trap')
plt.xlabel('N')
plt.ylabel('Error in integral approx')
plt.legend()
