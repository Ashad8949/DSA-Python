# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 13:53:43 2022

@author: Ashad Alam

Circular Queue 
"""
class Queue:
    # initialization TC: O(1) , SC: O(n)
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize 
        self.start = -1 
        self.top = -1 
        
    # function to print 
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True 
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False 
        
    def isEmpty(self):
        if self.top == -1:
            return True 
        else:
            return False 
        
    def enque(self, val):
        if self.isFull():
            return "The LL is Empty"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0 
            self.items[self.top] = val
            return "The element is inserted at the end of Queue"
        
    def deque(self):
        if self.isEmpty():
            return " Queue is Empty"
        else:
            first = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1 
                self.top = -1 
                
            elif self.start + 1 == self.maxSize:
                self.start = 0
                
            else:
                self.start += 1
            self.items[start] = None 
            return first
        
    def peak(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            return self.items[self.start]
        
    def delete(self):
        self.items = [None]* self.maxSize
        
que = Queue(3)
print(que.isFull())
que.enque(1)
que.enque(2)
que.enque(3)
print(que.isEmpty())
print(que.deque())
print(que.peak())
print(que)
            
        
    
        
    
