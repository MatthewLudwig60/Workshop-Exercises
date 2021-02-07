#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:05:00 2020

@author: Matthew
"""
a = []
number = 1
status = False
while status == False:
    n = int(input('What number would you like all the positive odd terms up to?'))
    if int(n/2) != float(n/2):
        status = True
    else:
        status = False
while number <= n:
    a.append(number)
    number = number + 2
print(a)