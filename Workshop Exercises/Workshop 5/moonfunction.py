#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:03:08 2020

@author: Matthew
"""
earth_weight = 52
def moon_weight_calculate(earth_weight, timespan, weight_gain):
    for year in range(1, (timespan+1)):
        earth_weight = earth_weight + weight_gain
        moon_weight = earth_weight * 0.165
        print('In year {} your weight is {}N'.format(year, moon_weight))
moon_weight_calculate(float(input('How much do you weigh on Earth?')), int(input('For how many years will you stay on the Moon?')), float(input('How much weight do you gain a year?')))
