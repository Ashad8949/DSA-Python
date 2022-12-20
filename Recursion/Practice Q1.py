# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:53:03 2022

@author: Ashad Alam
"""

def productOfArray(arr):
    i = len(arr)
    if i==1:
        return arr[0]
    else:
        arr1 = arr[:i-1]
        return arr[i-1]*productOfArray(arr1)

print(productOfArray([1,3,2]))