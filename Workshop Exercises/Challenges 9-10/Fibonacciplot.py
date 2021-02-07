#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:00:45 2020

@author: Matthew
"""
import matplotlib.pyplot as plt
def Fibonacci(first_term, second_term, number_terms, label):
    terms = [float(first_term), float(second_term)]
    index = []
    ratios = []
    for i in range(int(number_terms)):
        terms.append(terms[-1]+terms[-2])
        ratio = terms[-1] / terms[-2]
        ratios.append(ratio)
    for i in range(int(number_terms)):
        index.append(i)
    plt.plot(index, ratios, label = '{}'.format(label))
plt.figure()
Fibonacci(0, 1, 100, '0, 1')
Fibonacci(17, 23, 100, '17, 23')
plt.legend()