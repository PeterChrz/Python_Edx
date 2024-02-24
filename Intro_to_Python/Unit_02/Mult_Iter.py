#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 04:40:03 2024

@author: pch
"""

def mult_iter(a, b):
    result = 0 
    while b > 0:
        result += a
        b -= 1
    return result


def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)
    
## Mathematical Induction
# To prove a statement indexed on integers is true for all values of n
# prove it's true for n at it's smallest value (n = 0 or n = 1)
# Then prove it's true for an arbitrary value and n+1