#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:05:24 2021

@author: Matthew
"""

import numpy as np 
def MatrixSolver(A, b): #defines function to solve a matrix equation of the form Ax = b
    detA = np.linalg.det(A) #finds determinant of A
    if abs(detA)<1e-20:
        print('This matrix is singular with a determinant of 0. The system of equations cannot be solved.')
    else: 
        if abs(detA)<0.01: #Tests if determinant is close to zero in magnitude so whether matrix is poorly conditioned
            print('This matrix is poorly conditioned with a determinant of ' + str(detA)) 
        else: 
            print('This matrix has a determinant of ' + str(detA))
            Ainv = np.linalg.inv(A) #Finds inverse of A
            x = np.dot(Ainv, b) #Finds dot product of inverse of A and b to give x
            print('The array of x values is')
            print(x)
            test = np.dot(A, x) #Finds dot product of A and calculated values for x, checks this gives b 
            print('The test values are')
            print(test)
            print('and the actual values are')
            print(b)
            status = True
            for i in range(len(b)):
                if abs(test[i] - b[i]) > 1e-8:
                    status = False
            if status == True:
                print('The test was a success') #If this evaluates to b, calculated values for x are accurate
            else: 
                print('The test was a failure') #If not, calculated values for x are inaccurate 
        

rows_A = int(input('How many rows does matrix A have?')) #User inputs shape of matrix A
columns_A = int(input('How many columns does matrix A have?'))

A = np.zeros((rows_A, columns_A)) #Sets up matrix of the shape defined by the user
A_elements = input('What are the elements of the matrix of coefficients?') #Creates list of coefficients of matrix
A_elements = A_elements.split() #Splits string of coefficients into list of individual coefficients
for i in range(len(A_elements)):
    A_elements[i] = float(A_elements[i])  #Converts coefficients from strings to floats
for i in range(rows_A):
    for j in range(columns_A):
        index = columns_A * i + j
        A[i,j] = A_elements[index] #Assigns coefficients to matrix A
        
b = np.zeros(rows_A) #Sets up vector of shape no. rows of A x 1
b_elements = input('What are the elements of b?') #User inputs elements of b
b_elements = b_elements.split()
for i in range(len(A_elements)):
    A_elements[i] = float(A_elements[i])
for i in range(rows_A):
    b[i] = b_elements[i] #Elements of b are split, converted into floats and assigned to vector b

MatrixSolver(A,b) #Calls function matrix solver passing it arguments matrix A and vector b

    
        