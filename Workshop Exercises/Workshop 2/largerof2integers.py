#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:21:05 2020

@author: Matthew
"""

integer1 = int(input('What is your 1st number?'))
integer2 = int(input('What is your 2nd number?'))
if integer1 > integer2:
    print('The larger number is ' + str(integer1))
elif integer1 == integer2:
    print('Your 2 numbers are equal')
else:
    print('The larger number is ' + str(integer2))