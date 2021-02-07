#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 19:52:56 2020

@author: Matthew
"""

'''
Example Code for Getting started

A useful thing to know, anything to the right of a # will not be read by the
code. This is useful for making comments. The same is true for anything 
between sets of three quotation marks this is
useful for longer comments (such as this one)

Press F5 or click the green play button to run the code (this will require 
you to save the code)
'''

a = 1
b = 1.0
c = "Hello"
# In the terminal on the right (if using Spyder) run the command
# type(a), type(b) and type(c).


d = [a, b, c]
# Notice how this list can contain other variables, not just
# direct inputs. The elements of the list do not have to be the same type.
# d[0] will return the value of a, d[1] will return value of b etc.

# We can manually edit a list. For example, in the terminal type "d".
# After this try typing d[0] = a number of your choice
# Now type "d" again


e = (1.0, a, c, c, "356")
# e is a tuple so cannot be editted the same way.
# Try the same process as for d and notice you only get an error message.


""" Using Python to perform matrix operations """
import numpy as np

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[5,6],[7,8]])

array3 = np.add(array1, array2) 
# This is an addition of like elements (each position
# adds with the equivalent position on the other matrix)
# This is only possible for arrays of the same shape
print("array3 = \n", array3, "\n")
# \n tells Python to insert an empty line to the "print" statement
print(np.shape(array3), "\n")

array4 = np.multiply(array1, array2)
print("array4 = \n", array4, "\n")
array5 = np.dot(array1, array2)
print("array5 = \n", array5, "\n")
# Notice the "multiply" command is also element wise, however,
# the "dot" command is the dot product (how we usually refer to multiplication
# matricies in maths)
# This is how numpy offers a "divide" command even though this is not possible
# in normal matrix maths.

"""The Transpose Function"""
# Sometimes a command operates of a specific object type
# It is called with object.command such as the example below
array6 = array1.T
# This effectively reverses the position columns and rows


""" BONUS TASK: try to understand the code below showing how to manually 
perform a transpose using loops. You don't need to understand this yet, but
if you can even roughly understand whats going on its great """

array7 = np.array([[1,2],[3,4],[5,6]]) # Making a new array

s = np.shape(array7) # Shape is a 2x3, so s = (3,2) [Vertical axis comes first]

new_array = np.zeros((s[1],s[0]))

for i in range(s[0]):       # For the length of first axis (3)
    for j in range(s[1]):   # For the length of the second axis (2)
        new_array[j][i] = array7[i][j]
        
print("new_array = \n", new_array, "\n")
print("array7 = \n", array7.T)

""" In this piece of code, effectively I tell Python: for each number of
elements on the first "i" axis and each number of elements on the second "j"
axis, the new array has the (i,j) value of the original array at the (j,i)
position in the new array """