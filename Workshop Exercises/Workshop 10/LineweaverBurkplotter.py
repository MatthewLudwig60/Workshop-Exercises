#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:59:50 2021

@author: Matthew
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
rates = input('Input your rate data in moldm^-3s^-1')
rates = rates.split()
for i in range(len(rates)):
    rates[i] = float(rates[i])
concs = input('Input your conc data in moldm^-3')
concs = concs.split()
for i in range(len(concs)):
    concs[i] = float(concs[i])

plt.figure()
plt.plot(concs, rates)
plt.xlabel('Concentration/moldm^-3')
plt.ylabel('Rate/moldm^-3s^-1')

conc_array = np.zeros((len(concs)))
for i in range(len(concs)):
    conc_array[i] = concs[i]
rate_array = np.zeros((len(rates)))
for i in range(len(rates)):
    rate_array[i] = rates[i]

inv_conc = (conc_array)**(-1)
inv_rate = (rate_array)**(-1)
plt.figure()
plt.plot(inv_conc, inv_rate, 'r+')
linreg = ss.stats.linregress(inv_conc, inv_rate)
plt.plot(inv_conc, (linreg[0]*inv_conc + linreg[1]))
plt.xlabel('1/[S] / dm^3mol^-1')
plt.ylabel('1/rate / dm^3mol^-1s^-1')
Vmax = (linreg[1])**(-1)
Km = Vmax * linreg[0]
print('Km = ' + str(Km) + ' and Vmax = ' + str(Vmax) + ' moldm^-3s^-1')