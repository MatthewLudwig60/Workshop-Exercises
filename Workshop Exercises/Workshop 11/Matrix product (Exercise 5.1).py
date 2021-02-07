#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:01:53 2021

@author: Matthew
"""

import numpy as np
def matrixproduct(A,B):
    rows_A = np.shape(A)[0]
    columns_A = np.shape(A)[1]
    rows_B = np.shape(B)[0]
    columns_B = np.shape(B)[1]
    if columns_A != rows_B:
        P = 'Matrices cannot be multiplied'
    else:
        P = np.zeros((rows_A, columns_B))
        for i in range(rows_A):
            for j in range(columns_B):
                P[i,j] = 0
                for k in range(columns_A):
                    P[i,j] += A[i,k]*B[k,j]
                P[i,j] = P[i,j]
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

