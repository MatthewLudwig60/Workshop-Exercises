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
        multiplier = 1
        for i in range(len(numbers)):
            multiplier = multiplier * numbers[i]
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
                    position_number_status = False
                    while position_number_status == False:
                        position_number = position_number - 28
                        if position_number < 29:
                            position_number_status = True
                    letters[i] = characters[(position_number)]
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
        decrypted_message = ''
        for i in range(len(letters)):
            decrypted_message += str(letters[i])
        print(decrypted_message)
        
            
        