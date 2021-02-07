#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:18:25 2020

@author: Matthew
"""

def collatz(start_term, number_terms):
    terms = [float(start_term)]
    counter = 0
    while counter < int(number_terms)-1:
        if terms[-1] % 2 == 0:
            term = terms[-1] / 2
        else:
            term = 3*terms[-1] + 1
        terms.append(term)
        counter+=1
    return terms
#for i in range(1, 21):
    #print(collatz(i, 20))


def collatz2(start_term, number_terms):
    terms = [float(start_term)]
    counter = 0
    while counter < int(number_terms)-1:
        if terms[-1] % 2 == 0:
            term = terms[-1] / 2
        else:
            term = 3*terms[-1] - 1
        terms.append(term)
        counter+=1
    return terms
for i in range(1, 21):
    print(collatz2(i, 20))
