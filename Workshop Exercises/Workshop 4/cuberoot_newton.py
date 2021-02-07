#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:20:43 2020

@author: Matthew
"""

x = 5
y = x/2
eps = float(input('What is your accepted tolerance?'))
counter = 0
while abs(y**3 - x) > eps:
    y = y - ((y**3 - x)/(3*(y**2)))
    counter += 1
    print(y)
print('After {} iterations, an approximation for the cube root of {} is {}'.format(counter, x, y))