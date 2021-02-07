#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:28:29 2021

@author: Matthew
"""

import numpy as np
almost_ones = np.ones((5, 6))
for i in range(5):
    for j in range(6):
        if i == j:
            almost_ones[i, j] = 0
        print('i = {}, j = {}, almost_ones = {}'.format(i, j, almost_ones[i, j]))
