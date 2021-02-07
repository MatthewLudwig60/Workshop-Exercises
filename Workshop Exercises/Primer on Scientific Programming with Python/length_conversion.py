#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:38:21 2020

@author: Matthew
"""

length_metres = float(input('What is the length in metres?'))
length_inches = (length_metres/0.0254)
length_feet = ((length_inches)/12)
length_yards = ((length_feet)/3)
length_miles = ((length_yards)/1760)
length_metres = str(length_metres)
length_inches = str(length_inches)
length_feet = str(length_feet)
length_yards = str(length_yards)
length_miles = str(length_miles)
print('The length is ' + length_metres + ' metres, ' + length_inches + ' inches, ' + length_feet + ' feet, ' + length_yards + ' yards and ' + length_miles + ' miles.' )