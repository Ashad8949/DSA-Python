# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 06:57:26 2022

@author: Ashad Alam
"""

def FirstMethod():
    SecondMethod()
    print("First Method")

def SecondMethod():
    ThirdMethod()
    print("Second Method")
    
def ThirdMethod():
    FourthMethod()
    print("Third Method")

def FourthMethod():
    print("Fourth Method")
    
FirstMethod()
