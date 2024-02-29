#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:58:00 2024

@author: pch
"""

def fib(x):
    if x == 0 or x == 1: 
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
    
print(fib(12))