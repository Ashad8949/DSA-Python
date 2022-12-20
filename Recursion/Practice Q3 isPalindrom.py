# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 18:55:35 2022

@author: Ashad Alam
"""

def isPalindrome(strng):
    def Reverse(strng):
        if len(strng)==1:
            return str(strng[0])
        return str(strng[len(strng)-1])+str(Reverse(strng[:len(strng)-1]))
    
    if Reverse(strng)==strng:
        return "true"
    return "false"

print(isPalindrome("eottboe"))