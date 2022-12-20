# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 07:27:49 2022

@author: Ashad Alam
"""

def pSubseq(arr, idx, S):
    if idx == len(arr):
        # cond satisfied
        if S == 3:
            return 1
        # cond not satisfied
        
        return 0
    # take 
    S += arr[idx]
    l = pSubseq(arr, idx + 1, S)
    # not take 
    S -= arr[idx]
    r = pSubseq(arr, idx + 1, S)
    
    return l + r

arr = [3, 1, 2]
idx = 0
S = 0
print(pSubseq(arr, idx, S))