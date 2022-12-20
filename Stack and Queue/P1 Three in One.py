# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:25:16 2022

@author: Ashad Alam

P: 1 
Description: Three in One
"""

class Multistack:
    def __init__(self, stacksize):
        self.numberstacks = 3 
        self.custList = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks 
        self.stacksize = stacksize
        
    def isFull(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True 
        else:
            return False 
        
    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True 
        else:
            return False 
        
    def indexofTop(self, stacknum):
        offset = stacknum * self.stacksize 
        return offset + self.sizes[stacknum] - 1
    
    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return "The stack is Full"
        else:
            self.sizes[stacknum] += 1 
            self.custList[self.indexofTop(stacknum)] = 0
            self.sizes[stacknum] -= 1 
            return value 
        
    def pop(self, sta)
        
    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.custList[self.indexofTop(stacknum)]
            return value 
       