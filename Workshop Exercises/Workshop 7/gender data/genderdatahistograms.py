#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:24:30 2020

@author: Matthew
"""

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('01_heights_weights_genders.csv')

byGender = data.groupby('Gender')
boys = byGender.get_group('Male')
girls = byGender.get_group('Female')


fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=True)
fig.suptitle('Plots of frequency density of heights for the entire population, men and women')
axs[0].hist(data['Height'], 80)
axs[1].hist(boys['Height'], 80)
axs[2].hist(girls['Height'], 80)