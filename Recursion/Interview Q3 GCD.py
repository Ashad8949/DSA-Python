# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:36:37 2022

@author: Ashad Alam
"""

def GCD(A,B):
    assert int(A)==A and int(B)==B,"Number should be integer"
    if A<0:
        A=-1*A
    if B<0:
        B=-1*B
    if A%B==0:
        return B
    return GCD(B,A%B)

print(GCD(49,14))