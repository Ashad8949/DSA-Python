# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 15:10:40 2022

@author: Ashad Alam
"""

class Node:
    def __init__(self, value = None):
        self.value = value 
        self.head = None 
        self.tail = None 
        
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
        node.next = None 
        node.prev = None 
        self.head = node 
        self.tail = node 
        
    def insert(self, value, position):
        if self.head is None:
            return "LL is Empty"
        else:
            newNode = Node(value)
            
            if position == 0:
                newNode.prev = None 
                newNode.next = self.head 
                self.head.prev = newNode 
                self.head = newNode 
                
            elif position == 1:
                newNode.next = None 
                newNode.prev = self.tail 
                self.tail.next = newNode 
                self.tail = newNode 
                
            else:
                tempNode = self.head 
                index = 0
                while index < position - 1:
                    tempNode = tempNode.next 
                    index += 1
                nextNode = tempNode.next 
                newNode.next = nextNode
                newNode.prev = tempNode 
                tempNode.next = newNode 
                nextNode.prev = newNode 
                
DLL = DoublyLL()
DLL.create(5)

DLL.insert(0,0)
DLL.insert(2,1)

print([node.value for node in DLL])
                