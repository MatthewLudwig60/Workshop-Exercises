#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:23:09 2020

@author: Matthew
"""
def find_root(y, power, eps):
    num_guesses = 0
    tot_guesses = 100
    low = 0
    high = max(1, y) #returns larger of 1 and y
    ans = (high + low) / 2 #average of entire interval

    while abs(ans**(power) - y) >= eps and num_guesses < tot_guesses:
        print('L = {} H= {} ANS = {}'.format(low, high, ans))
        num_guesses += 1
        if ans**(power) < y:
            low = ans #if guess is smaller than root, set LB of interval to current guess
        else:
            high = ans #if guess is larger than root, set UB of interval to current guess
        ans = (high + low) / 2 #set new guess to middle of new interval

    print('num_guesses = {}'.format(num_guesses))
    if power == 2:
        print('{} is close to square root of {}'.format(ans, y))
    elif power == 3:
        print('{} is close to cube root of {}'.format(ans, y))
    else:
        print('{} is close to {}th root of {}'.format(ans, power, y))
find_root(float(input('What would you like to find the root of?')), int(input('Which root would you like to find?')), float(input('What is your accepted tolerance?')))