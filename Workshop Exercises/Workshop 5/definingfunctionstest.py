#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:39:43 2020

@author: Matthew
"""
def add_lists(x0, x1):
    if len(x0) == len(x1):
        x_add = []
        for i in range(len(x0)):
            x_add.append(x0[i] + x1[i])
        return x_add
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(add_lists(l1, l2))

