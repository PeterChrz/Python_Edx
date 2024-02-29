#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:27:15 2024

@author: pch
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if b == 0:
      return a
    else:
      return gcdRecur(b, a % b)
        
print(gcdRecur(6, 12))