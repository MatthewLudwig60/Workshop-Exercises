#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:04:31 2020

@author: Matthew
"""

y = 25 
eps = .001
num_guesses = 0
tot_guesses = 100
low = 0
high = max(1, y) #returns larger of 1 and y
ans = (high + low) / 2 #average of entire interval

while abs(ans**3 - y) >= eps and num_guesses < tot_guesses:
    print('L = {} H= {} ANS = {}'.format(low, high, ans))
    num_guesses += 1
    if ans**3 < y:
        low = ans #if guess is smaller than root, set LB of interval to current guess
    else:
        high = ans #if guess is larger than root, set UB of interval to current guess
    ans = (high + low) / 2 #set new guess to middle of new interval

print('num_guesses = {}'.format(num_guesses))
print('{} is close to cube root of {}'.format(ans, y))