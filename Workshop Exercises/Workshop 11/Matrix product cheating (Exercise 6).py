#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:20:12 2021

@author: Matthew
"""

import numpy as np
def matrixproduct(A,B):
    P = np.dot(A,B)
    print(P)
rows_A = int(input('How many rows does matrix A have?'))
columns_A = int(input('How many columns does matrix A have?'))

A = np.zeros((rows_A, columns_A))

A_elements = input('What are the elements of A?')
A_elements = A_elements.split()
for i in range(len(A_elements)):
    A_elements[i] = float(A_elements[i])
for i in range(rows_A):
    for j in range(columns_A):
        index = columns_A * i + j
        A[i,j] = A_elements[index]
        
rows_B = int(input('How many rows does matrix B have?'))
columns_B = int(input('How many columns does matrix B have?'))
B = np.zeros((rows_B, columns_B))

B_elements = input('What are the elements of B?')
B_elements = B_elements.split()
for i in range(len(B_elements)):
    B_elements[i] = float(B_elements[i])
for i in range(rows_B):
    for j in range(columns_B):
        index = columns_B * i + j
        B[i,j] = B_elements[index]
        
matrixproduct(A,B)