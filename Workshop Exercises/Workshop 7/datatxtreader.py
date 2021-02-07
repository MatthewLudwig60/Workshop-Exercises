#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:15:45 2020

@author: Matthew
"""

data = open('data.txt')
status = True
while status == True:
    line = data.readline()
    if not line:
        status = False
    else:
        print('{}'.format(float(line)/2))
data.close()
   
