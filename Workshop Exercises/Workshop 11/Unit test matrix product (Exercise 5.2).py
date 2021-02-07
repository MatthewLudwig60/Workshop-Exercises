#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:04:23 2021

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
    return(P)
def testingfunction(N):
    actualmatrixproduct = np.identity(N)
    testmatrixproduct = matrixproduct(np.identity(N), np.identity(N))
    print('The matrix product is =\n', actualmatrixproduct)
    print('The test output is =\n', testmatrixproduct)
    equivalence = True
    for i in range(N):
        for j in range(N):
            if actualmatrixproduct[i,j] != testmatrixproduct[i,j]:
                equivalence = False
    if equivalence == True:
        print('The test is successful')
    else:
        print('The test is a failure')
    
        
testingfunction(2)