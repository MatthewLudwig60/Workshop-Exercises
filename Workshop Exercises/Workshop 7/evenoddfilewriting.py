#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:56:57 2020

@author: Matthew
"""
myf1 = open('odd.dat', 'w')
myf2 = open('even.dat', 'w')
for i in range(101):
    if i%2 != 0:
        myf1.write('{}\n'.format(i))
    else:
        myf2.write('{} \n'.format(i))
myf1.close()
myf2.close()

        
        
        
        