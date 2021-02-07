#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:59:23 2021

@author: Matthew
"""

import numpy as np
import matplotlib.pyplot as plt
def oceanwaves(t, x):
    return np.exp(-t/4) * np.cos(10*2*np.pi*x-t)


def shipwaves(t, x):
    return 0.4*np.exp(-t/6) * np.sin(3*2*np.pi*x-t)

def waves(t, x):
    return oceanwaves(t, x) + shipwaves(t, x)

nx = 100
x = np.linspace(0, 1, nx)
nt = 1
t = np.linspace(0, 5, nt) # number of time points
Wavesintime = np.zeros((nt, nx))
Wavesintime2 = np.zeros((nt, nx))
for iT in range(nt):
    for iX in range(nx):
        Wavesintime[iT, iX] = waves(t[iT], x[iX])
for iT in range(nt):
    for iX in range(nx):
        Wavesintime2[iT, iX] = oceanwaves(t[iT], x[iX])
for iT in range(nt):
    plt.plot(x, Wavesintime[iT, :]) # for each timepoint, plot amplitude across all displacement points
    plt.plot(x, Wavesintime2[iT, :]) #blue = w/ ship waves, orange = w/o ship waves