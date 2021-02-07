#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:21:16 2021

@author: Matthew
"""
import numpy as np
a = float(input('What is real component of your complex number?'))
b = float(input('What is the imaginary component of your complex number?'))
z = a + b*1j
modulus = np.sqrt(a**2 + b**2)
if a>0 and b!=0:
    arg = np.arctan(b/a)
elif a>0 and b == 0:
    arg = 0
elif a == 0 and b == 0:
    arg = 'undefined'
elif a == 0 and b>0:
    arg = (np.pi)/2
elif a == 0 and b<0:
    arg = -(np.pi)/2
elif a < 0 and b > 0:
    arg = np.pi - np.arctan(abs(b/a))
elif a < 0 and b < 0:
    arg = -(np.pi) + np.arctan(abs(b/a))
# argstatus = False
# while argstatus == False:
#     if arg > -(np.pi) and arg <= np.pi:
#         argstatus = True
#     else: 
#         if arg <= -(np.pi):
#             arg = arg + 2*(np.pi)
#         elif arg > np.pi:
#             arg = arg - 2*(np.pi)
#         if arg > -(np.pi) and arg <= np.pi:
#             argstatus = True
        
print('The modulus of complex number ' + str(z) + ' is ' + str(modulus) + ' and its argument is ' + str(arg))
    