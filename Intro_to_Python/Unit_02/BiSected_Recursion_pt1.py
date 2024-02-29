#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:32:53 2024

@author: pch
"""
def isIn(char, aStr):
    def sortWord(aStr):
      return ''.join(sorted(aStr.lower()))

    def findIt(char, sortedString):
        if len(sortedString) == 0:
            return False
        
        mid = len(sortedString) // 2
        
        if char.lower() == sortedString[mid]:
            return True
        else:
            if char.lower() < sortedString[mid]:
                return findIt(char, sortWord(sortedString[:mid]))
            else:
                return isIn(char, sortWord(sortedString[mid+1:]))
            
    return findIt(char, sortWord(aStr))

print(isIn('Z', 'Pizzatastic'))
