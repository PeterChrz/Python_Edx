#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:02:56 2024

@author: pch
"""

def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            print(str(s[0]), str(s[1]), str(s[-1]))
            return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))


print(isPalindrome("RaCeTcAr"))