# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:09:33 2022

@author: Ashad Alam

Queue
"""

class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True 
        else:
            return False 
        
    def enqueue(self, value):
        self.items.append(value)
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.items.pop(0)
        
    def peak(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = []



que = Queue()
print(que.isEmpty())

que.enqueue(1)
que.enqueue(2)
que.enqueue(3)

print(que)

print(que.dequeue())
print(que.peak())

print(que)