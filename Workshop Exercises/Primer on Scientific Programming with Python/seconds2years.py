#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:33:02 2020

@author: Matthew
"""

lifeexpect_years = 82.51
lifeexpect_seconds = (lifeexpect_years * 365.25 * 24 * 3600)
if lifeexpect_seconds > 1000000000:
    print('A baby can expect to live for 1 billion seconds.')
else:
    print('A baby cannot expect to live for 1 billion seconds.')