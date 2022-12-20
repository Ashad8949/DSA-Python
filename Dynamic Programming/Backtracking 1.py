# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 02:23:25 2022

@author: Ashad Alam

1 -- N by back-tracking
"""

def prt(i, n):
    if i < 1:
        return 
    #print(i)        #recursion
    prt(i-1, n)
    print(i)        #backtracking
    
prt(5,5)


def prt(i, n):
    if i > n:
        return 
    prt(i+1, n)
    print(i)
    
prt(1, 5)
