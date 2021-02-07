#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:54:02 2021

@author: Matthew
"""

import numpy as np
import numpy as np
def dot(u,v):
    u_array = np.zeros(len(u))
    for i in range(len(u)):
        u_array[i] = u[i]
    v_array = np.zeros(len(v))
    for i in range(len(v)):
        v_array[i] = v[i]
    sum = 0
    if len(u_array) != len(v_array):
        sum = 'Error, lengths of input vectors inequal'
    else:
        for i in range(len(u_array)):
            sum += u_array[i] * v_array[i]
    return(sum) 

    
def testingfunction(N):
    u = np.ones(N)
    v = np.ones(N)
    actualdotproduct = N
    print('The dot product is ' + str(actualdotproduct))
    testdotproduct = dot(u,v)
    print('The output of the test function is ' + str(testdotproduct))
    error = abs(float(actualdotproduct) - float(testdotproduct))
    if error < 1e-5:
        print('The test was successful')
    else:
        print('The test was a failure')
testingfunction(6)