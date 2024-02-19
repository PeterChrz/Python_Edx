#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:04:44 2024

@author: pch
"""
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Calculate the monthly interest rate
monthlyInterestRate = annualInterestRate / 12.0

# Iterate over 12 months
for month in range(12):
    # Calculate the minimum monthly payment
    minimumMonthlyPayment = monthlyPaymentRate * balance

    # Calculate the monthly unpaid balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment

    # Calculate the updated balance for the next month
    updatedBalance = monthlyUnpaidBalance * (1 + monthlyInterestRate)

    # Update the balance for the next iteration
    balance = updatedBalance

# Print the remaining balance after one year
print(f"Remaining balance: {balance:.2f}")