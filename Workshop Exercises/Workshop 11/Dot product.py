#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:48:19 2021

@author: Matthew
"""
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
    print(sum) 
u = [1, 2, 3]
v = [3, 2, 1]
dot(v, u)
        