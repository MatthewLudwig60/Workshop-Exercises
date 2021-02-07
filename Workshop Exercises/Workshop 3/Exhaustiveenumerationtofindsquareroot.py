#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:25:37 2020

@author: Matthew
"""

x = 25
epsilon = 0.01 #tolerance
step = epsilon**2 #amount we increase our guess by 
num_guesses = 0
tot_guesses = 1e7 #total number of iterations permitted before we give up
ans = 0
while abs(ans**2 - x) >= epsilon and num_guesses <= tot_guesses: #iterate if the difference between our guess and the answer is greater than the tolerance
    ans += step 
    num_guesses += 1
print(f'Num Guesses: {num_guesses}')
if abs(ans**2 - x) >= epsilon:
    print(f'Failed to find sqrt of {x}')
else:
    print(f' {ans} is close to sqrt of {x}')