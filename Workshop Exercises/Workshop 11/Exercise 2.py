#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:45:45 2021

@author: Matthew
"""
import numpy as np
A_elements = input('What are the elements of vector A?')
A_elements = A_elements.split()
for i in range(len(A_elements)):
    A_elements[i] = float(A_elements[i])
A = np.zeros(len(A_elements))
for i in range(len(A_elements)):
    A[i] = A_elements[i]
dotproduct = np.dot(A, A)
multiplyproduct = A*A
print('The dot product of A with itself is ' + str(dotproduct) + 'whilst the output of A * A is ' + str(multiplyproduct))