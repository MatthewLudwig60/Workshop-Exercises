#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:09:56 2020

@author: Matthew
"""

x = 25
y = x/2
eps = float(input('What is your accepted tolerance?'))
counter = 0
while abs(y**2 - x) > eps:
    y = y - ((y**2 - x)/(2*y))
    counter += 1
    print(y)
print('After {} iterations, an approximation for the square root of {} is {}'.format(counter, x, y))