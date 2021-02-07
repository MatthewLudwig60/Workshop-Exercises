#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:45:29 2020

@author: Matthew
"""

import numpy as np
import pylab as plt
N = 6 #number of strips
a = 0 #LB of integral
b = 2 #UB of integral
x = np.linspace(a, b, N) #Generates N equally spaced values from a to b
h = x[1] - x[0] #strip width = 2nd x value - 1st x value
def functionwewanttointegrate(x):
    #define function we want to integrate
Integraloffunction = 0
for k in range(N):
    Integraloffunction += functionwewantointegrate(x[k]) 
Integraloffunction = Integraloffunction * h

