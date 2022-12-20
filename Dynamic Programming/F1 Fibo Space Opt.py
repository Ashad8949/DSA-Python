# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 01:36:14 2022

@author: Ashad Alam
"""

def fibo(n):
    prev, prev1 = 0, 1
    for i in range(2, n+1):
        curr = prev + prev1
        prev1, prev = curr, prev1 
    return prev

print(fibo(5))