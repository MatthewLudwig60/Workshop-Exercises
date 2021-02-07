#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:32:26 2020

@author: Matthew
"""

terms = [1, 1]
counter = 0
while counter <= 7:
    term = terms[-1] + terms[-2]
    terms.append(term)
    counter += 1
print(terms)
