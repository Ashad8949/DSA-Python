# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 18:48:08 2022

@author: Ashad Alam
"""

class Node:
    def __init__(self, value = None):
        self.value = value 
        self.next = None 
        
class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None 
        
    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            if node.next == self.head:
                break
            node = node.next 
            
    def create(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node 
        self.tail = node
        return "CSLL has been created"
        
CSLL = CircularSLL()
CSLL.create(1)

print([node.value for node in CSLL])
        