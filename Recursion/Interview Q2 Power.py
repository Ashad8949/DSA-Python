# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:33:49 2022

@author: Ashad Alam
"""

def Power(a,n):
    assert n>=0 and int(n) ==n,"exp must be positive integer"
    if n==0:
        return 1
    return a*Power(a,n-1)

print(Power(-2,5))