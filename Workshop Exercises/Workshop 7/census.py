#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:24:03 2020

@author: Matthew
"""

import pandas as pd
import matplotlib.pyplot as plt
census = pd.read_csv('census.csv')
print(type(census))
print(census.head())
print(census.tail())
print(census['2011'])
print('Minimum 2011 : {}'.format(census['2011'].min()))
print('Maximum 2011 : {}'.format(census['2011'].max()))
print('Average 2011 : {}'.format(census['2011'].mean()))
print(census[census['State'] == 'New York'])
census['Growth'] = census['2012'] - census['2011']
print(census.head())