#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:44:51 2021

@author: Matthew
"""
import numpy as np 
A_elements = input('What are the elements of your vector?')
A_elements = A_elements.split('i')
A = np.zeros((((len(A_elements)-1), 1)), dtype='complex128')
for i in range(len(A_elements)-1):
    place = A_elements[i]
    place = place.split('+')
    a = float(place[0])
    b = float(place[1])
    z = a + b*1j
    A[i] = z
print(A)
