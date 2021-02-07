#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:17:33 2021

@author: Matthew
"""
import numpy as np
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Vector ({self.x}, {self.y})'
    def __add__(self, other):
        return Vector((self.x + other.x) , (self.y + other.y)) 
    def length(self):
        return np.sqrt((self.x)**2 + (self.y)**2)
v1 = Vector(2, 3)
v2 = Vector(1, 5)

print(v1.__add__(v2))
print(v1.length())