# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:17:09 2022

@author: Ashad Alam
"""

def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
    if len(arr)==1:
        return isOdd(arr[0])
    return isOdd(arr[0]) or someRecursive(arr[1:],cb)
arr=[22,2,4]
cb = "cb"
print(someRecursive(arr, cb))