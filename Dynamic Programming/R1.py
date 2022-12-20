# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:48:41 2022

@author: Ashad Alam
"""

def Reverse(arr, l, r):
    if l == r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    Reverse(arr, l+1, r-1)
    return arr
                          
arr = [1, 2, 3, 4, 5]
l = 0
r = len(arr)-1
Reverse(arr, l, r)
print(arr)