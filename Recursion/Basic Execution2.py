# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 07:14:13 2022

@author: Ashad Alam
"""

def RM(n):
    if n<1:
        print("n is less than 1")
    else:
        RM(n-1)
        print(n)

RM(5)