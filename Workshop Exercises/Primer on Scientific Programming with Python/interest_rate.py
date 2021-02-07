#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:48:18 2020

@author: Matthew
"""

initial_sum = float(input('How much money are you starting with?'))
interest_rate = float(input('What is your interest rate?'))

status = False
while status == False:
    time = float(input('How long will you invest for?'))
    if time != int(time):
        status = False
    else:
        status = True
        
final_sum = initial_sum * ((1 + (interest_rate / 100))**time)
initial_sum = str(initial_sum)
time = str(time)
interest_rate = str(interest_rate)
final_sum = str(final_sum)
print('Your final sum after investing £' + initial_sum + ' for ' + time + ' years at ' + interest_rate + '% interest is £' + final_sum)
