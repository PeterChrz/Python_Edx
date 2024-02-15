#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 18:29:21 2024

@author: pch
"""
low = 0
high = 100
valid_chars = {"h", "c", "l"}

print("Please think of a number between 0 and 100! ")  # Initial instruction

while True:
    gnum = (low + high) // 2

    print("Is your secret number " + str(gnum) + "?")

    while True:  # Add an inner loop for input validation
        response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.").lower()  # Convert input to lowercase for easier comparison
        if response in valid_chars:
            break  # Exit inner loop if input is valid
        else:
            print("Sorry, I did not understand your input.")  
            print("Is your secret number " + str(gnum) + "?")

    if response == 'c':
        print("Game over. Your secret number was: ", gnum)  # Use gnum here  
        break
    elif response == 'h':
        high = gnum
    elif response == 'l':
        low = gnum
