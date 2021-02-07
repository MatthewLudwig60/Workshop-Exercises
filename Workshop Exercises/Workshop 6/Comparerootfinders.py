#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:50:25 2020

@author: Matthew
"""
def bisection_root(x, eps):
    num_guesses = 0
    tot_guesses = 100
    low = 0
    high = max(1, x) #returns larger of 1 and y
    ans = (high + low) / 2 #average of entire interval

    while abs(ans**3 - x) >= eps and num_guesses < tot_guesses:
        num_guesses += 1
        if ans**3 < x:
            low = ans #if guess is smaller than root, set LB of interval to current guess
        else:
            high = ans #if guess is larger than root, set UB of interval to current guess
        ans = (high + low) / 2 #set new guess to middle of new interval
    print('After {} iterations, an approximation for the cube root of {} is {}'.format(num_guesses, x, ans))
    data = [ans, num_guesses]
    return data
    

def newton_root(x, eps):
    ans = x/2
    num_guesses = 0
    while abs(ans**3 - x) > eps:
        ans = ans - ((ans**3 - x)/(3*(ans**2)))
        num_guesses += 1
    print('After {} iterations, an approximation for the cube root of {} is {}'.format(num_guesses, x, ans))
    data = [ans, num_guesses]
    return data

def algorithm_Evaluation(x, eps):
    bisection_data = (bisection_root(x, eps))
    bisection_answer = bisection_data[0]
    bisection_iterations = bisection_data[1]
    bisection_accuracy = (abs(bisection_answer - x**(1/3)) / x**(1/3)) * 100
    print(f'The bisection algorithm required {bisection_iterations} iterations giving the root with a percentage error of {bisection_accuracy}% with an accepted tolerance of {eps}')
    
    newton_data = newton_root(x, eps)
    newton_answer = newton_data[0]
    newton_iterations = newton_data[1]
    newton_accuracy = (abs(newton_answer - x**(1/3)) / x**(1/3)) * 100
    print(f'The Newton Raphson algorithm required {newton_iterations} iterations giving the root with a percentage error of {newton_accuracy}% with an accepted tolerance of {eps}')

for i in range(1,16):
    print(f'What is the cube root of {i}?')
    algorithm_Evaluation(i, 0.01)
    print(' ')
