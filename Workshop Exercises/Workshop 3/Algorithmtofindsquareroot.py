#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:25:37 2020

@author: Matthew
"""

x = 25
epsilon = 0.001
step = epsilon**2
num_guesses = 2
tot_guesses = 1e7
ans = 0
while abs(ans**2 - x) >= epsilon and num_guesses <= tot_guesses:
    ans += step
    num_guesses += 1
print(f'Num Guesses: {num_guesses}')
if abs(ans**2 - x) >= epsilon:
    print(f'Failed to find sqrt of {x}')
else:
    print(f' {ans} is close to sqrt of {x}')