# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 01:22:19 2022

@author: Ashad Alam
"""

def fibo(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n-1]

print(fibo(4))