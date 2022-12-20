# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 07:25:04 2022

@author: Ashad Alam
"""

def Power(n):
    if n==0:
        return 1
    else:
        power=Power(n-1)
        return power*2
    
print(Power(5))


def Power(n):
    p=1
    while n>0:
        p=p*2
        n-=1
    return p
print(Power(5))