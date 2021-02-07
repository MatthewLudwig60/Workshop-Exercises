#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:39:25 2020

@author: Matthew
"""
myf = open('Mydatafile.txt', 'w')
for i in range(10):
    myf.write('{}\n'.format(i))
myf.close()