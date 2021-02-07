#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:26:56 2020

@author: Matthew
"""
import numpy as np

def areacalc(a, b, c):
    s = 0.5*(a+b+c)
    area = (s*(s-a)*(s-b)*(s-c))**(0.5)
    return area
def areacalc2(a, b, x):
    area = 0.5 * a * b * np.sin(np.pi*x/180)
    return area
answer = input('Do you have 3 sides or 2 sides and an angle? (3sides/2sides)')
if answer == '3sides':
    x1 = float(input('How long is your first side?'))
    x2 = float(input('How long is your second side?'))
    x3 = float(input('How long is your third side?'))
    area = areacalc(x1, x2, x3)
elif answer == '2sides':
    x1 = float(input('How long is your first side?'))
    x2 = float(input('How long is your second side?'))
    x3 = float(input('How large is the angle between the sides?'))
    area = areacalc2(x1, x2, x3)
print('The area of your triangle is {}'.format(area))
    

    
    