# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 15:56:14 2022

@author: Ashad Alam
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        

class singlyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next 
    
    def insert(self,value, location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode 
                
            else:
                tempNode = self.head  
                index = 0
                while index< location -1:
                    tempNode = tempNode.next 
                    index+=1
                nextNode = tempNode.next 
                tempNode.next = newNode
                newNode.next = nextNode 
                
    def traverseLL(self):
        if self.head is None:
            print("The Singly Linked List DNE")
            
        else:
            node = self.head 
            while node is not None:
                print(node.value)
                node = node.next
            
SLL = singlyLinkedList()
SLL.insert(1,1)
SLL.insert(2,1)
SLL.insert(3,1)
SLL.insert(4,1)

SLL.insert(0,0)

print([node.value for node in SLL])
SLL.traverseLL()
                
        
        
    