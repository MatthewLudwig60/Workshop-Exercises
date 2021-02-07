#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:25:15 2020

@author: Matthew
"""
import pandas as pd
data = pd.read_csv('census.csv')

data['growth'] = data['2012'] - data['2011']
data['% change'] = ((data['2012'] - data['2011']) / data['2011']) * 100
#print(data.head())
#print(data['2011'].max())
#print(data['2011'].min())
#print(abs(data['growth']).max())
states = data['State']
year2011 = data['2011']
growthdata = data['growth']
changedata = data['% change']
maxstate = states[0]
minstate=states[0]
maxreductstate = states[0]
maxchangestate = states[0]
for i in range(0, len(states)):
    if data['2011'].max() == year2011[i]:
        maxstate = states[i]
    if data['2011'].min() == year2011[i]:
        minstate = states[i]
    if data['growth'].min() == growthdata[i]:
        maxreductstate = states[i]
    if data['% change'].max() == changedata[i]:
        maxchangestate = states[i]
print('The state with the largest population in 2011 was {} with a population of {}'.format(maxstate, data['2011'].max()))
print('The state with the smallest population in 2011 was {} with a population of {}'.format(minstate, data['2011'].min()))
print('The state with the largest decrease in population from 2011 to 2012 was {} with a population change of {}'.format(maxreductstate, data['growth'].min()))
print('The state with the largest percentage change in population from 2011 to 2012 was {} with a population change of {}%'.format(maxchangestate, data['% change'].max()))
