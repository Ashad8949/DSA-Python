# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 10:52:24 2022

@author: Ashad Alam
"""

class Node:
    def __init__(self, value=None):
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
    
    def create(self, value):
        node = Node(value)
        node.next = node 
        self.head = node 
        self.tail = node 
        return "Node has been created"
    
    def insert(self, value, position):
        if self.head is None:
            return "LL is Empty" 
        else:
            newNode = Node(value)
            if position == 0:
                newNode.next = self.head 
                self.head = newNode
                self.tail.next = newNode 
                
            elif position == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode 
                
            else:
                tempNode = self.head 
                index = 0
                while index < position - 1:
                    tempNode = tempNode.next 
                    index += 1
                nextNode = tempNode.next 
                tempNode.next = newNode
                newNode.next = nextNode
                
    def traversal(self):
        if self.head is None:
            return "LL is Empty"
        else:
            node = self.head 
            while node:
                print(node.value)
                node = node.next 
                if node == self.tail.next:
                    break
    
    def search(self, target):
        if self.head is None:
            return "LL is Empty"
        else:
            tempNode = self.head 
            while tempNode:
                if tempNode.value == target:
                    return True
                tempNode = tempNode.next 
                if tempNode == self.tail.next:
                    return False
    # Node Deletion            
    def delete(self, location):
        if self.head is None:
            return"LL is empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None 
                    self.tail = None
                    
                else:
                    self.head = self.head.next 
                    self.tail.next = self.head
                    
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None 
                    self.tail = None
                    
                else:
                    node = self.head 
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next 
                    node.next = self.head 
                    self.tail = node 
                    
            else:
                tempNode = self.head 
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next 
                tempNode.next = nextNode.next
                
    # ENTIRE LL DELETION           
    def DEL(self):
        self.head = None
        self.tail = None 
                
CSLL = CircularSLL()
print(CSLL.create(1))
CSLL.insert(0,0)
CSLL.insert(2,1)
CSLL.insert(3,1)
CSLL.insert(2,2)
print([node.value for node in CSLL])
print(CSLL.traversal())
print(CSLL.search(3))
CSLL.delete(0)

print([node.value for node in CSLL])

CSLL.DEL()
print([node.value for node in CSLL])
                    