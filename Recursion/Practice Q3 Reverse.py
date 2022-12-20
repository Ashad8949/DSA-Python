# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 18:08:39 2022

@author: Ashad Alam
"""

def Reverse(strng):
    if len(strng)==1:
        return str(strng[0])
    return str(strng[len(strng)-1])+str(Reverse(strng[:len(strng)-1]))

print(Reverse("Python"))