# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 14:59:19 2022

@author: Ashad Alam
"""

class Node:
    def __init__(self, value = None):
        self.value = value 
        self.prev = None 
        self.next = None 
        
class DoublyLL:
    def __init__(self):
        self.head = None 
        self.tail = None 
        
    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next 
            
    def create(self, value):
        node = Node(value)
        node.prev = None 
        node.next = None 
        self.head = node 
        self.tail = node
        return "Dll has been Created" 
    
DLL = DoublyLL()
DLL.create(2)
print([node.value for node in DLL])
    