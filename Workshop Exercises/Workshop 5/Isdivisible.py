#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:52:53 2020

@author: Matthew
"""

def isdivisible(x, y):
    if x / y == 1:
        return True
    else:
        return False
x = float(input('What is your first number?'))
y = float(input('What is your second number?'))
if isdivisible(x, y) == True:
    print('{} is divisible by {}'.format(x, y))
elif isdivisible(x, y) == False:
    print('{} is not divisible by {}'.format(x, y))
