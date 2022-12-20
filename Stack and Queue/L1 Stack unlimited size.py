# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 10:50:14 2022

@author: Ashad Alam

Stack without size limit

-- Easy to implement 
-- Speed problem when it grows
"""

# create a stack class
class Stack:
    def __init__(self):
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
    
    def push(self, value):
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
        
    
stack = Stack()

print(stack.isEmpty())
stack.push(1)
stack.push(3)
stack.push(2)

#print(stack)
print("---")
print(stack.peek())
print("---")
print(stack.pop())
print("----")
stack.delete()
print(stack)
        
        