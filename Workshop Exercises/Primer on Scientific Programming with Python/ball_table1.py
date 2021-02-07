#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:23:01 2020

@author: Matthew
"""
initial_velocity = float(input('What is the initial velocity?'))
n = int(input('How many intervals of time?'))
times = []
vertical_displacements = []
for i in range(n+1):
    times.append((i/n) * ((2 * initial_velocity) / 9.81))
for i in range(len(times)):
    y = initial_velocity * times[i] - 0.5 * 9.81 * ((times[i])**2)
    if y < 0.00001:
        y = 0
    vertical_displacements.append(y)
for i in range(len(times)):
    print('t: ' + str(times[i]) + ' y: ' + str(vertical_displacements[i]))
    