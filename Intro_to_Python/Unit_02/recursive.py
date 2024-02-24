#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:25:24 2024

@author: pch
"""

def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

print(mult_iter(3, 3))

def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)
    
print(mult(3, 3))

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(4))

## Recursion works on creating new scopes, not changing the previous scope but once 
## the value hits 1, it goes back to the previous scope passing return values 
## like dominos falling backwards. Combining the result as it goes.
## 24 =  4 * 3 *  2 * 1 

def factorial_iter(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i 
    return prod

print(factorial_iter(4))

## Iteration maybe more efficient for the computer but recursion can be more human readable and understandable. 