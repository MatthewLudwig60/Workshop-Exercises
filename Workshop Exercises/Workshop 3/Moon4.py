#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:19:45 2020

@author: Matthew
"""

earth_weight = 52
for year in range(1,16):
    earth_weight = earth_weight + 1
    moon_weight = earth_weight * 0.165
    if moon_weight > 10.5:
        print('Your weight has reached a fatal level!')
        break
    print('In year {} your weight is {}'.format(year, moon_weight))