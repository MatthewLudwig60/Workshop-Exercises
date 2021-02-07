#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:47:56 2021

@author: Matthew
"""

import numpy as np
import matplotlib.pyplot as plt
def implicit_euler(func, y0, timestep, UB, funcsolved):
    num_points = int((UB/timestep)+1)
    timepoints = np.linspace(0, UB, num_points)
    datapoints = np.zeros(num_points)
    datapoints[0] = y0
    for i in range(num_points-1):
        x0 = datapoints[i]
        def auxfunc(func, timestep, y, t, const):
            return timestep*func(y, t) - y + const
            
        error = abs(auxfunc(func, timestep, x0, timepoints[i+1], datapoints[i]))
        while error > 0.01:
            x0 = x0 - ((timestep*auxfunc(func, timestep, x0, timepoints[i+1], datapoints[i]))/(auxfunc(func, timestep, (x0+0.5*timestep), timepoints[i+1], datapoints[i])-auxfunc(func, timestep, (x0-0.5*timestep), timepoints[i+1], datapoints[i])))
        datapoints[i+1] = x0
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

implicit_euler(func1, -1, 0.1, 2, func1solved)