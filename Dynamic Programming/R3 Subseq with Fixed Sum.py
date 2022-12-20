# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 07:04:02 2022

@author: Ashad Alam
"""

def pSubseq(arr, idx, ans, S):
    if idx == len(arr):
        if S == 3:
            print(ans)
        return 
    # take 
    ans.append(arr[idx])
    S += arr[idx]
    pSubseq(arr, idx + 1, ans, S)
    # not take 
    ans.pop()
    S -= arr[idx]
    pSubseq(arr, idx + 1, ans, S)

arr = [3, 1, 2]
ans = []
idx = 0
S = 0
pSubseq(arr, idx, ans, S)