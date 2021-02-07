#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:55:54 2020

@author: Matthew
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
string2 = 'hij'
result = alphabet.index('hij')
result2 = alphabet.index('opq')
print(alphabet[0:(result)] + alphabet[(result+3):result2] + alphabet[(result2 + 3):-1])