# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 20:20:27 2022

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
            node = node.next 
            if node == self.tail.next:
                break 
            
    def create(self, nodeValue):
        node = Node(nodeValue)
        node.next = node 
        self.head = node 
        self.tail = node 
        return "LL has been created"
        
    def insert(self , value, location):
        if self.head is None:
            return "The head is None"
        
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head 
                self.head = newNode 
                self.tail.next = newNode 
                
            elif location == 1:
                newNode.next = self.tail.next 
                self.tail.next = newNode 
                self.tail = newNode 
                
            else:
                tempNode = self.head 
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next 
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode 
                newNode.next = nextNode 
            return "the node has been inserted"
                
    def traversal(self):
        if self.head is None:
            print("Empty LL")
            
        else:
            tempNode = self.head 
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next 
                if tempNode == self.tail.next:
                    break 
   
CSLL = CircularSLL()
print(CSLL.create(1))
CSLL.insert(0,0)
CSLL.insert(2,1)
CSLL.insert(3,1)
CSLL.insert(2,2)
print([node.value for node in CSLL])
print(CSLL.traversal())