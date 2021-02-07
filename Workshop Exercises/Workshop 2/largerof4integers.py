#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 12:56:03 2020
Gives largest of 4 integers with bubble sort
@author: Matthew
"""
integers = []
counter = 0
while counter <=10:
    integers.append(int(input('What is your number?')))
    counter = counter + 1
status = False
while status == False:    
    corrections = 0
    for i in range(len(integers)-1):
        
        if integers[i] > integers[i+1]:
            x = integers[i]
            integers[i] = integers[i+1]
            integers[i+1] = x
            corrections = corrections + 1
    print(integers)
    if corrections == 0:
        status = True 
print(integers[-1])
        
        
