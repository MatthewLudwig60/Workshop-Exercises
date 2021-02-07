#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:02:54 2021

@author: Matthew
"""

import numpy as np
import matplotlib.pyplot as plt
def explicit_euler(func, y0, timestep, UB, funcsolved):
    num_points = int((UB/timestep)+1)
    timepoints = np.linspace(0, UB, num_points)
    datapoints = np.zeros(num_points)
    datapoints[0] = y0
    for i in range(num_points-1):
        datapoints[i+1] = datapoints[i] + func(datapoints[i], timepoints[i])*timestep
    plt.plot(timepoints, datapoints)
    actualdata = funcsolved(timepoints)
    plt.plot(timepoints, actualdata)
    plt.legend(['Numerical plot','Analytical plot'])
    plt.xlabel('t')
    plt.ylabel('y')
    



def func1(y, t):
    return (np.exp(t-t**2)-2*t*y)
def func1solved(t):
    return (np.exp(t-t**2) -2*np.exp(-(t**2)))

def func2(y, t):
    return (-30*y)
def func2solved(t):
    return (np.exp(-30*t))

explicit_euler(func1, -1, 0.05, 2, func1solved)

explicit_euler(func2, 1, 0.1, 1, func2solved) #solver doesn't work for this function as this is a 'stiff' ODE