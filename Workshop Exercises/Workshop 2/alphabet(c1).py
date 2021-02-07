#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:41:05 2020

@author: Matthew
"""
def split(word):
    return[char for char in word]
word = 'abcdefghijklmnopqrstuvwxyz'
letters = split(word)
print(letters)
string2 = 'hij'
result = int(word.index('hij'))
print(result)
letters.pop()[(result):(result+2)]
print(str(letters))

