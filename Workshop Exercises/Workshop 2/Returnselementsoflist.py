#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:26:48 2020

@author: Matthew
"""

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [16, 2, 43, 22., .11116, 2./3., 72.]
list3 = ['a', 'b', '63']
list4 = ['abcde', '54']
list5 = []
list5.append(list1)
list5.append(list2)
list5.append(list3)
list5.append(list4)
for i in range(len(list5)):
    print(list5[i][0], list5[i][-1])
    

