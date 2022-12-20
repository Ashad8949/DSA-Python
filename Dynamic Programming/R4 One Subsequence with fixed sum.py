# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 07:18:22 2022

@author: Ashad Alam
"""

def pSubseq(arr, idx, ans, S):
    if idx == len(arr):
        # cond satisfied
        if S == 3:
            print(ans)
            return True
        # cond not satisfied
        
        return False
    # take 
    ans.append(arr[idx])
    S += arr[idx]
    if pSubseq(arr, idx + 1, ans, S):
        return True
    # not take 
    ans.pop()
    S -= arr[idx]
    if pSubseq(arr, idx + 1, ans, S):
        return True

arr = [3, 1, 2]
ans = []
idx = 0
S = 0
pSubseq(arr, idx, ans, S)