# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:37:50 2022

@author: Ashad Alam
"""

# create a stack class
class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
        
    def __str__(self):
        values = self.list.reverse() 
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True 
        else:
            return False
        
    def isFull(self):
        if len(self.list) == maxSize:
            return True
        return False
    
    def push(self, value):
        if self.isFull():
            return "Stack is Full"
        else:
            self.list.append(value)
        
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        self.list = []
        
    
stack = Stack(4)

print(stack.isEmpty())
print(stack.isFull())
stack.push(1)
stack.push(3)
stack.push(2)

print(stack)
print("---")
print(stack.peek())
print("---")
print(stack.pop())
print("----")
stack.delete()
print(stack)