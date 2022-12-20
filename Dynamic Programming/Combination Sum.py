# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:13:56 2022

@author: Ashad Alam
"""

class Solution:
    def Comb(self, arr, target, idx, ans, sub):
        if idx == len(arr):
            if target == 0:
                print(sub)
                ans.append(sub)
                print(ans)
            return 
        # take 
        if arr[idx] <= target:
            sub.append(arr[idx])
            self.Comb(arr, target - arr[idx], idx, ans, sub)
            sub.pop()
        self.Comb(arr, target, idx+1, ans, sub)
        
    def combinationSum(self, candidates, target):
        idx = 0
        ans = []
        subArr = []
        self.Comb(candidates, target, idx, ans, subArr)
        return ans
    
S = Solution()
candidates = [2,3,6,7]
target = 7
print(S.combinationSum(candidates, target))
