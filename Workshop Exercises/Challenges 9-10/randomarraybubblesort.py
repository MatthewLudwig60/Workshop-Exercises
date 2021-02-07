#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:09:56 2020

@author: Matthew
"""
import random as rnd
counter = 0
terms = []
while counter<1000:
    terms.append(rnd.randint(-10, 10))
    counter +=1
print(terms)
status = False
while status == False:
    time = 0
    for i in range(1, len(terms)):
        if terms[i] < terms[i-1]:
            dummy = terms[i-1] 
            terms[i-1] = terms[i]
            terms[i] = dummy
            time +=1
    if time == 0:
        status = True
print(terms)
            
    