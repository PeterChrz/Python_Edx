#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:00:20 2024

@author: pch
"""

num = 19
start = num

if num < 0:
    isNeg = True
    num = abs(num)
else: 
    isNeg = False
    
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = '-' + result
    
print("The binary of " + str(start) + " is " + result)