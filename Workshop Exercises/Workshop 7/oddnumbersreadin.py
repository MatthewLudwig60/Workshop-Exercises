#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:10:24 2020

@author: Matthew
"""

myf = open('odd.dat')
numbers = []
while True:
    line = myf.readline()
    if not line:
        break
    else:
        numbers.append(line[0:-1])
print(numbers)
myf.close()