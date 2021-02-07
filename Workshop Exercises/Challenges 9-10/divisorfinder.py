#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:04:51 2020

@author: Matthew
"""

def divisorfinder(x):
    divisors = []
    for i in range(1, x+1):
        if x%i == 0:
            divisors.append(i)
    if divisors == [1, x]:
        return x
primes = []
for i in range(1, 10001):
    if divisorfinder(i) != None:
        primes.append(divisorfinder(i))
print(primes)
    
     
