# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 11:59:42 2022

@author: Ashad Alam
"""

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        
class Singlylikedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head 
        while node:
            yield node
            node = node.next
            
    def insert(self,value,position):
        newNode = Node(value)
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode 
            
        else:
            if position == 0:
                newNode.next = self.head 
                self.head = newNode 
            
            elif position == 1:
                self.tail.next = newNode 
                self.tail = newNode
                
            else:
                tempNode = self.head 
                index = 0
                while index < position-1:
                    tempNode = tempNode.next 
                    index+=1
                nextNode = tempNode.next 
                tempNode.next = newNode
                newNode.next = nextNode 
    
    def traverse(self):
        if self.head is None:
            print("LL is empty")
            
        else:
            node = self.head 
            while node is not None:
                print(node.value)
                node = node.next
                
    def search(self,target):
        if self.head is None:
            return "DNE"
        
        else:
            node = self.head 
            while node is not None:
                if node.value == target:
                    return node.value 
                node = node.next 
            return -1
        
SLL = Singlylikedlist() 
SLL.insert(1, 1)    
SLL.insert(2, 1)
SLL.insert(3, 1)
SLL.insert(4, 1)

SLL.insert(0, 0) 
SLL.insert(-1, 4)

print([node.value for node in SLL])
print(SLL.traverse())
print(SLL.search(-1))
        
        
            
    