#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:40:50 2020

@author: Matthew
"""

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('01_heights_weights_genders.csv')
plt.scatter(data['Weight'], data['Height'])