#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 13:57:29 2020

@author: Matthew
"""
import time
difficulty = input('Which difficulty would you like to try? (easy/medium/hard)')
if difficulty == 'easy':
    passage = 'Closed captions were created for deaf or hard of hearing individuals to assist in comprehension. They can also be used as a tool by those learning to read, learning to speak a non-native language, or in an environment where the audio is difficult to hear or is intentionally muted.'
if difficulty == 'medium':
    passage = 'There are many idiosyncratic typing styles in between novice-style hunt and peck and touch typing. For example, many hunt and peck typists have the keyboard layout memorized and are able to type while focusing their gaze on the screen. Some use just two fingers, while others use 3-6 fingers. Some use their fingers very consistently, with the same finger being used to type the same character every time, while others vary the way they use their fingers.'
elif difficulty == 'hard':
    passage = 'A virtual assistant (typically abbreviated to VA) is generally self-employed and provides professional administrative, technical, or creative assistance to clients remotely from a home office.'
word_counter = 1
for i in range(len(passage)):
    if passage[i] == ' ':
        word_counter += 1
status = False
while status == False:
    prompt = input('Are you ready yet? (y/n)')
    if prompt == 'y':
        status = True
        Time1 = time.time()
        total_characters = len(passage)
        print('Copy the following passage')
        print(passage)
        guess = input()
        Time2 = time.time()
        counter_correct = 0
        for i in range(len(passage)):
            if passage[i] == guess[i]:
                counter_correct += 1
        if len(guess) > len(passage):
            percentage_correct = (counter_correct / len(guess)) * 100
        else:
            percentage_correct = (counter_correct / total_characters) * 100
        Time_elapsed = Time2 - Time1
        print('You completed the ' + difficulty + ' typing test of ' + str(word_counter) + ' words in ' + str(Time_elapsed) + ' seconds with a percentage accuracy of ' + str(percentage_correct))           
    else:
        status = False
