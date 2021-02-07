#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:14:33 2020

@author: Matthew
"""

earth_weight = 52
for year in range(1,26):
    if year%2 == 0:
        earth_weight = earth_weight + 1
    moon_weight = earth_weight * 0.165
    print('In year {} your weight on Earth is {} and your weight on the Moon is {}'.format(year, earth_weight, moon_weight))
    