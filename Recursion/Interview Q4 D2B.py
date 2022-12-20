# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:48:42 2022

@author: Ashad Alam
"""

def D2B(n):
    assert int(n)==n,"Must be Integer"
    if n==0:
        return 0
    return n%2 + 10*D2B(n//2)

print(D2B(32))