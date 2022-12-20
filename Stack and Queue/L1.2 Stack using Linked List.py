# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 19:08:12 2022

@author: Ashad Alam
"""

class Node:
    def __init__(self, value = None):
        self.value = value 
        self.next = next 
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next 
        
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
        
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True 
        else:
            return False 
        
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next 
            return nodeValue
        
    def peak(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
        
    def delete(self):
        self.LinkedList.head = None
        
stack = Stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack.peak())



        