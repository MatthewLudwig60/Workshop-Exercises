#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:51:45 2021

@author: Matthew
Program gives wave amplitude with displacement at different points in time from t=0 to t=1
"""

import numpy as np
import matplotlib.pyplot as plt
def oceanwaves(t, x):
    return np.exp(-t/4) * np.cos(10*2*np.pi*x-t)
nx = 100
x = np.linspace(0, 1, nx)
nt = 10
t = np.linspace(0, 5, nt) # number of time points
Wavesintime = np.zeros((nt, nx))

for iT in range(nt):
    for iX in range(nx):
        Wavesintime[iT, iX] = oceanwaves(t[iT], x[iX])
for iT in range(nt):
    plt.plot(x, Wavesintime[iT, :]) # for each timepoint, plot amplitude across all displacement points