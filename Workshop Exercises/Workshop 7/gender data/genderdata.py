#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:54:00 2020

@author: Matthew
"""

import pandas as pd
data = pd.read_csv('01_heights_weights_genders.csv')
print(data.head())
byGender = data.groupby('Gender') #groups data points by the gender column data
print(byGender.size()) #gives size of 2 gender groups
print(byGender.mean()) # gives mean values of other characteristics for 2 gender groups
boys = byGender.get_group('Male') #ascribes all male data to new dataframe boys
print(boys.head())