#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:57:23 2020

@author: Matthew
"""

a = float(input('What is the coefficient of x^2?'))
b = float(input('What is the coefficient of x?'))
c = float(input('What is the constant term?'))
if (b**2 - 4*a*c) > 0:
    x1 = -((-b + ((b**2 - 4*a*c)**0.5))/(2*a))
    x2 = -((-b - ((b**2 - 4*a*c)**0.5))/(2*a))
    print('The roots of the equation are ' + str(x1) + ' and ' + str(x2))
if (b**2 - 4*a*c) == 0:
    x = -((-b + ((b**2 - 4*a*c)**0.5))/(2*a))
    print('The repeated root of the equation is ' + str(x))
if (b**2 - 4*a*c) < 0:
    x1 = -((-b + ((-(b**2 - 4*a*c))**0.5))/(2*a))
    x2 = -((-b - ((-(b**2 - 4*a*c))**0.5))/(2*a))
    print('The roots of the equation are ' + str(x1) + 'i and ' + str(x2) + 'i')