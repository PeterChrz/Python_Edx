#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:30:37 2024

@author: pch
"""

def g(x):
    def h():
        x = 'abc'
        return x
    x = x + 1
    print('in g(x): x = ', x)
    x = h()
    return x

x = 3
print(g(x))