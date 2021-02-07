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
A_elements = input('What are the elements of vector A?')
A_elements = A_elements.split()
for i in range(len(A_elements)):
    A_elements[i] = float(A_elements[i])
A = np.zeros(len(A_elements))
for i in range(len(A_elements)):
    A[i] = A_elements[i]
    
B_elements = input('What are the elements of vector B?')
B_elements = B_elements.split()
for i in range(len(B_elements)):
    B_elements[i] = float(B_elements[i])
B = np.zeros(len(B_elements))
for i in range(len(B_elements)):
    B[i] = B_elements[i]
dot(A, B)
        