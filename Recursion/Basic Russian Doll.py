# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 06:30:42 2022

@author: Ashad Alam
"""

def RussianDoll(doll):
    if doll == 1:
        print("All Doll are opened")
    else:
        RussianDoll(doll-1)

RussianDoll(6)
