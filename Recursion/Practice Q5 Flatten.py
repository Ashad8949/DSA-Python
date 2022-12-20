# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:50:41 2022

@author: Ashad Alam
"""

def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
            print(resultArr)
        else: 
            resultArr.append(custItem)
    return resultArr

print(flatten([[[[[1,2]],3],4],5]))
