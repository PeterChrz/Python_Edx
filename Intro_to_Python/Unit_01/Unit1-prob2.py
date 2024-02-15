#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:48:20 2024

@author: pch
"""

s = 'azcbobobegghakl'


count = sum(1 for i in range(len(s) - 2) if s[i:i+3] == 'bob')

print("Number of times bob occurs is: " + str(count))