#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:49:53 2020

@author: Matthew
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
string2 = 'hij'
result = alphabet.index('hij')
print(alphabet[0:(result)] + alphabet[(result+3):-1])
