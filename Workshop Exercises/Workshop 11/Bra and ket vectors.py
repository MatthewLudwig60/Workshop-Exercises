#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 13:29:36 2021

@author: Matthew
"""

import numpy as np

def complexconjugate(z):
    zbar = z.real + z.imag*(-1)*1j
    return zbar
def compleximaginary(A):
    Atrp = np.transpose(A)
    for i in range(len(Atrp)):
        Atrp[i] = complexconjugate(Atrp[i])
    return(Atrp)


value = input('Is your vector a bra or a ket? (bra/ket)')
A_elements = input('What are the elements of your vector?')
A_elements = A_elements.split('i')
if value == 'ket':
    A = np.zeros((((len(A_elements)-1), 1)), dtype='complex128')
if value == 'bra':
    A = np.zeros(((1, (len(A_elements)-1))), dtype='complex128')
for i in range(len(A_elements)-1):
    place = A_elements[i]
    place = place.split('+')
    a = float(place[0])
    b = float(place[1])
    z = a + b*1j
    if value == 'ket':
        A[i] = z
    elif value == 'bra':
        A[0,i] = z

if value == 'ket':
    print('Your input ket vector is')
    print(A)
    print('The corresponding bra vector is')
    print(compleximaginary(A))
else:
    print('Your input bra vector is')
    print(A)
    print('The corresponding ket vector is')
    print(compleximaginary(A))
    
