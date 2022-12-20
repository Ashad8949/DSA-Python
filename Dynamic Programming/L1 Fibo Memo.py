# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 01:08:46 2022

@author: Ashad Alam

Memoization
"""

def fibo(n, dp):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if not n in dp:
        dp[n] = fibo(n-1, dp) + fibo(n-2, dp)
    return dp[n]

dp = {}
print(fibo(4,dp))
        