#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:51:04 2020

@author: Matthew
"""

def Fibonacci(first_term, second_term, number_terms):
    terms = [float(first_term), float(second_term)]
    for i in range(int(number_terms)-2):
        terms.append(terms[-1]+terms[-2])
        ratio = terms[-1] / terms[-2]
    return ratio
print(Fibonacci(0, 1, 1001))
print(Fibonacci(17, 23, 1001))