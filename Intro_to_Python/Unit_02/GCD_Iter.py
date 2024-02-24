#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 05:15:26 2024

@author: pch
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
  
    if a < b: 
        a, b = b, a
    
    d = b
    
    while d > 0:
        if a % d == 0 and b % d == 0:
            return d
        d -= 1
    
    return 1
    
'''   
    largest = 0
    
    if a > b:
        for i in range(abs(b)):
            if a % i == 0 & i > largest:
                largest = i
    elif b > a:
        for i in range(abs(a)):
            if b % i == 0 & i > largest:
                largest = i
    return largest
'''

print(gcdIter(8, 4))