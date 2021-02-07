#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:09:43 2020

@author: Matthew
"""
import matplotlib.pyplot as plt
import numpy as np
def divisorfinder(x):
    divisors = []
    for i in range(1, x+1):
        if x%i == 0:
            divisors.append(i)
    if divisors == [1, x]:
        return x

def primedensity(N):
    primes = []
    for i in range(1, N+1):
        if divisorfinder(i) != None:
            primes.append(divisorfinder(i))
    Primedensity = len(primes) / N
    return Primedensity
data1 = []
data2 = []
for i in range(1, 10000, 1000):
    data1.append(i)
    data2.append(primedensity(i))
plt.figure()
plt.plot(data1, data2)