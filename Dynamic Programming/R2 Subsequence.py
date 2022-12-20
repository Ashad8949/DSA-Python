# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 06:58:45 2022

@author: Ashad Alam
"""

def pSubseq(arr, idx, ans):
    if idx == len(arr):
        print(ans)
        return 
    # take 
    ans.append(arr[idx])
    pSubseq(arr, idx + 1, ans)
    # not take 
    ans.pop()
    pSubseq(arr, idx + 1, ans)

arr = [3, 1, 2]
ans = []
idx = 0
pSubseq(arr, idx, ans)