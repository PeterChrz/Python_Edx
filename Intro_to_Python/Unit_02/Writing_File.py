#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:01:13 2024

@author: pch
"""

nameHandle = open('kids', 'w')

for i in range(2):
    name = input('enter name: ')
    nameHandle.write(name + " ")
nameHandle.close()

nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)
nameHandle.close()