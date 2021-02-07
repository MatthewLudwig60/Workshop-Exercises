#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:40:31 2020

@author: Matthew
"""
tolerance = float(input('What is your accepted tolerance?'))
for i in range(1, 26):
    guess = 1
    while abs(guess**2 - i) > tolerance:
        guess = (guess + (i/guess)) / 2
    print('The square root of {} is {}'.format(i, guess))
