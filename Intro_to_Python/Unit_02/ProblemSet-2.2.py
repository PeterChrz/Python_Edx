#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:34:02 2024

@author: pch
"""

balance = 4773
annualInterestRate = 0.2
fixedPayment = 0
def check_balance(balance, annualInterestRate, fixedPayment):
    
    flag = False
    month = 0
    while month < 12:
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = balance - fixedPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        month += 1
    if balance < 0:
        flag = True
    return flag
    
while not check_balance(balance, annualInterestRate, fixedPayment):
    fixedPayment += 10
    
    check_balance(balance, annualInterestRate, fixedPayment)

print("Lowest payment: ", fixedPayment)  