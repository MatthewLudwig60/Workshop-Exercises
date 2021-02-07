#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:14:16 2020

@author: Matthew
"""

myf = open('Mydatafile.txt', 'r')
while True:
    line = myf.readline()
    if not line:
        break
    else:
        print(line)
myf.close()

#or

myf = open('Mydatafile.txt', 'r')
data = myf.readlines()
print(data)
myf.close()
    
    
  