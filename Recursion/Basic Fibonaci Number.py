# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 09:43:56 2022

@author: Ashad Alam
"""

def Fabo(n):
    assert n>0 and int(n)==n,"The number must be Natural Number"
    if n==1:
        return 0
    if n==2:
        return 1
    return Fabo(n-1)+Fabo(n-2)

print(Fabo(5))