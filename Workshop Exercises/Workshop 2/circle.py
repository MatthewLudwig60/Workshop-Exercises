#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:41:15 2020

@author: Matthew
"""

import math
radii = [1.0, 20.0, 65.0, 70.0, 100.0]
for i in range(len(radii)):
    print('The circumference of a circle of radius ' + str(i) + 'cm is ' + str(2*i*math.pi) + 'cm')