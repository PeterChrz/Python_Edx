#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:06:09 2024

@author: pch
"""

balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12.0
test_balance = balance
lower_bound = balance / 12
upper_bound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
paided = False
while not paided:
    payment = (lower_bound + upper_bound) / 2
    for month in range(12):
        monthlyUnpaidBalance = test_balance - payment
        test_balance = monthlyUnpaidBalance + (monthlyInterestRate *
                                               monthlyUnpaidBalance)
    if test_balance < 0:
        upper_bound = payment
        test_balance = balance
    elif test_balance > 0.01:
        lower_bound = payment
        test_balance = balance
    elif 0 < test_balance < 0.01:
        paided = True
print("Lowest payment: ", round(payment, 2))