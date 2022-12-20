# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 12:24:12 2022

@author: Ashad Alam
"""

class Node:
    def __init__(self,value=None):
        self.value = value 
        self.next = None

class singly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node 
            node = node.next
            
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
                
            else:
                tempNode = self.head
                index = 0
                while index< location-1:
                    tempNode = tempNode.next 
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
                    
linked_list = singly_linked_list()
linked_list.insertSLL(1, 1)

print([node.value for node in linked_list])