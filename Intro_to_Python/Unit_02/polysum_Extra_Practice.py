#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:18:50 2024

@author: pch
"""

import math

def polysum(n, s):
    '''
    function calculates area of a polygon, the perimter and then the sum of the area and perimiter squared..
    Required inputs:
        n = number of sides
        s = length of each side
    '''
    area = ( (0.25*n*s**2)/(math.tan(math.pi/n)) )
    boundary = (n*s)**2
    sum = area + boundary
    
    # return four decimial places rounded. 
    return round(sum, 4)

# Example Run    
print(polysum(200,3))