#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:06:17 2020

@author: Matthew
"""

def split(word):
    return[char for char in word]
word = (input('Player 1, what is your word?'))
letters = split(word)
print(letters)
status = False
while status == False:
    readiness = input('Are you ready player 2?')
    if readiness == 'Yes' or readiness == 'yes' or readiness == 'Y' or readiness == 'y':
        status = True
    else:
        status = False
answer = []
for i in range(0, (len(letters))):
    answer.append('_')
print(answer)
guesses_remaining = len(letters) + 8
victory_state = False
guessed_letters = []
while guesses_remaining > 0:    
    guess = input('What is your guess player 2?')
    guessed_before_state = 0
    for i in range(0, len(guessed_letters)):
        if guess == guessed_letters[i]:
            guessed_before_state = guessed_before_state + 1
    if guessed_before_state > 0:
        print('You have already guessed this letter, guess again!')
    else:
        guessed_letters.append(guess)
        guess_state = 0
        for i in range(0, (len(letters))):
            if guess == letters[i]:
                letters.pop(i)
                letters.insert(i, '_')
                answer.pop(i)
                answer.insert(i, guess)
                print(answer)
                guess_state = guess_state + 1
        if guess_state == 0:
            print('Sorry, that is incorrect')
        guessed_counter = 0    
        for i in range(0, len(letters)):
            if letters[i] == '_':
                guessed_counter = guessed_counter + 1
            else:
                guessed_counter = guessed_counter
        if guessed_counter == len(letters):
            victory_state = True
        guesses_remaining = guesses_remaining - 1
        print('Guesses remaining: ' + str(guesses_remaining))
        print('You have guessed:')
        print(guessed_letters)
    if victory_state == True:
        print('You win')
        break 
if guesses_remaining == 0 and victory_state == False:
    print('You lose!')
       