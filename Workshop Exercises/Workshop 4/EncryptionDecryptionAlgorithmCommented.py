#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:44:13 2020

@author: Matthew
"""
status = False

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ',', '.']
def split(message):
            return[char for char in message]
# Naming of this function?
def sever(pin):
            return[int(char) for char in pin]
while status == False:
    prompt = input('Would you like to encrypt a message? (y/n)')
    if  prompt == 'y':
        status = True
        message = str(input('What is your message?'))
        letters = split(message)
        pin = input('What is your 4 number pin?')
        numbers = sever(pin)
        # Code to calculate multiplier should be made a function (as code is repeated later on)
        # Note that the code is not that secure, in that PINs 1234, 1243, 1432 etc. are all equivalent as they have the same product
        multiplier = 1
        for i in range(len(numbers)):
            multiplier = multiplier * numbers[i]

        # You shouldn't need to treat the a and . characters differently (see below)
        for i in range(len(letters)):
            if letters[i] == 'a':
                letters[i] = '!'
            elif letters[i] == '.':
                letters[i] = '?'
            else:
                
                j = characters.index(letters[i])
                position_number = j+multiplier
                if position_number < 29:
                    letters[i] = characters[(position_number)]
                else:
                    # You can use the modulo operator % for this
                    # See https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/
                    # See below for solution using %
                    position_number_status = False
                    while position_number_status == False:
                        position_number = position_number - 28
                        if position_number < 29:
                            position_number_status = True
                    letters[i] = characters[(position_number)]

        # To calculate new position for each character, use:
        
        # (characters.index(letters[i]) + multiplier) % 29

        # Using modulo 29 (% 29) will produce a remainder between 0 and 28 inclusive, which will always
        # translate into a single character in the characters array.

        # e.g.
        
        # Message = 'dave.'
        # PIN = 1284
        # multiplier = 64
        #
        # Message translates into new positions:
        
        # ((3  + 64) % 29) = 9  = 'j'
        # ((0  + 64) % 29) = 6  = 'g'
        # ((21 + 64) % 29) = 27 = ',' 
        # ((4  + 64) % 29) = 10 = 'k'
        # ((28 + 64) % 29) = 5  = 'f'

        # So encrypted message is 'jg,kf'
        
        encrypted_message = ''
        for i in range(len(letters)):
            encrypted_message += str(letters[i])
        print(encrypted_message)
    elif prompt == 'n':
        status = True
        print("Let's decrypt a message")
        code = str(input('What is your code?'))
        letters = split(code)
        pin = input('What was the 4 number pin used?')
        numbers = sever(pin)
        multiplier = 1
        for i in range(len(numbers)):
            multiplier = multiplier * numbers[i]
        for i in range(len(letters)):
            if letters[i] == '!':
                letters[i] = 'a'
            elif letters[i] == '?':
                letters[i] = '.'
            else:
                j = characters.index(letters[i])
                position_number = j-multiplier
                if position_number > (-1):
                    letters[i] = characters[(position_number)]
                else:
                    position_number_status = False
                    while position_number_status == False:
                        position_number = position_number + 28
                        if position_number > (-1):
                            position_number_status = True
                    letters[i] = characters[(position_number)]

        # To calculate new position for each character, use:
        
        # (characters.index(letters[i]) - multiplier) % 29

        # e.g.
        
        # Message = 'jg,kf'
        # PIN = 1284
        # multiplier = 64
        #
        # Message translates into new positions:
        
        # ((9  - 64) % 29) = 3  = 'd'
        # ((6  - 64) % 29) = 0  = 'a'
        # ((27 - 64) % 29) = 21 = 'v' 
        # ((10 - 64) % 29) = 4  = 'e'
        # ((5  - 64) % 29) = 28 = '.'

        # So decrypted message is 'dave.'
        
        decrypted_message = ''
        for i in range(len(letters)):
            decrypted_message += str(letters[i])
        print(decrypted_message)
        
            
        
