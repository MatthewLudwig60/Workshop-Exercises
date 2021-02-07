#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:22:39 2020

@author: Matthew
"""

import pandas as pd
import matplotlib.pyplot as plt
datax = pd.read_csv('rk4x.csv')
datay = pd.read_csv('rk4y.csv')
plt.figure()
plt.plot(datax, datay)