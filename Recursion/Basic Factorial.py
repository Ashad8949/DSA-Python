# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 09:05:43 2022

@author: Ashad Alam
"""

def Factorial(n):
    assert n>=0 and int(n)==0,"The number must be positive integer"
    if n==0:
        return 1
    return n*Factorial(n-1)
    
print(Factorial(5.3))