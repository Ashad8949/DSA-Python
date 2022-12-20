# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 18:05:21 2022

@author: Ashad Alam
"""

def Sum(n):
    if n==0:
        return 0
    return n+Sum(n-1)

print(Sum(10))