#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:57:41 2020

@author: Matthew
"""
def fibonacci(x):
    terms = [1, 1]
    counter = 0
    while counter <= (x-3):
        term = terms[-1] + terms[-2]
        terms.append(term)
        counter += 1
    return terms
y = int(input('How many terms of the Fibonacci sequence would you like?'))
print('The first {} terms of the Fibonacci sequence are {}'.format(y, fibonacci(y)))

    
