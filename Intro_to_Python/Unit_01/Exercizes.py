#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:50:21 2024

@author: pch
"""

num = 5
if num > 2:
    print(num)
    num -= 1
print(num)

# One shot run, it doesn't actully go into a loop like a for look,
# The if statement is just a branching so either/or path. 


for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')
        
        
count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)


num = 10
for num in range(5):
    print(num)
print(num)


divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 