#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:33:20 2021

@author: Matthew
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
times = input('Input your time data in seconds')
times = times.split()
for i in range(len(times)):
    times[i] = float(times[i])
concs = input('Input your conc data in moldm^-3')
concs = concs.split()
for i in range(len(concs)):
    concs[i] = float(concs[i])
    
plt.figure()
plt.plot(times, concs)
plt.xlabel('Time/s')
plt.ylabel('[A]/moldm^-3')

conc_array = np.zeros((len(concs)))
for i in range(len(concs)):
    conc_array[i] = concs[i]
time_array = np.zeros((len(times)))
for i in range(len(times)):
    time_array[i] = times[i]
    
#rate = k[A]
ln_conc = np.log(conc_array)
plt.figure()
plt.plot(time_array, ln_conc,  'r+')
plt.xlabel('Time/s')
plt.ylabel('ln([A]/moldm^-3)')
linreg1 = ss.stats.linregress(time_array, ln_conc)
plt.plot(time_array, (linreg1[0]*time_array + linreg1[1]))
pmcc1 = ss.stats.pearsonr(time_array, ln_conc)
pmcc1 = abs(pmcc1[0])

#rate = k[A]^2
inv_conc = (conc_array)**(-1)
plt.figure()
plt.plot(time_array, inv_conc, 'r+')
plt.xlabel('Time/s')
plt.ylabel('1/[A]/dm^3mol^-1')
linreg2 = ss.stats.linregress(time_array, inv_conc)
plt.plot(time_array, (linreg2[0]*time_array + linreg2[1]))
pmcc2 = ss.stats.pearsonr(time_array, inv_conc)
pmcc2 = abs(pmcc2[0])

if pmcc1 > pmcc2: #rate = k[A]
    initial_conc = np.exp(linreg1[1])
    k = -1 * linreg1[0]
    rate_model = 'k[A]'
    unit = 's^-1'
elif pmcc2 > pmcc1: #rate = k[A]^2
    initial_conc = (linreg2[1])**(-1)
    k = linreg2[0]
    rate_model = 'k[A]^2'
    unit = 'dm^3mol^-1s^-1'
print('The rate equation is ' + rate_model + ' with an initial conc [A]0 of ' + str(initial_conc) + ' moldm^-3 and a rate constant k = ' + str(k) + unit) 














