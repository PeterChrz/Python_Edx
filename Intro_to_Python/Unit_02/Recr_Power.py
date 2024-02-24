#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''


    if exp == 0:
        return 1.0
    else:
        return base * (recurPower(base, exp-1))
        
        
print(recurPower(-4.76, 4))