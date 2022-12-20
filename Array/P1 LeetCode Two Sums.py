# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:39:32 2022

@author: Ashad Alam
"""

class Solution:
    def twoSum(self, arr, target):
        seen = {}
        for i,value in enumerate(arr):
            diff = target-arr[i]
            if diff in seen:
                return (i,seen[diff])
            seen[value]=i
    
s = Solution()
arr=[2,7,11,15]
target = 9
print(s.twoSum(arr, target))