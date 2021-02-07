#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:18:42 2020

@author: Matthew
"""

earth_weight = 52
for year in range(1,16):
    earth_weight = earth_weight + 1
    moon_weight = earth_weight * 0.165
print('In year 15 your weight is ' + str(moon_weight))