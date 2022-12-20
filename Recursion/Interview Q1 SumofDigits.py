# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:15:25 2022

@author: Ashad Alam
"""

def SumOfDigits(n):
    assert n>=0 and int(n)==n,"Number must be Positive Integer"
    if n==0:
        return 0
    return n%10+SumOfDigits(n//10)

print(SumOfDigits(-12345))