# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 13:49:34 2022

@author: Ashad Alam
"""

class Node:
    def __init__(self,value=None):
        self.value = value 
        self.next = None 
        
class SinglyLikedList:
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
        if self.head is None:
            # LL is empty
            self.head = newNode 
            self.tail = newNode 
             
        else:
            # insertion at beginning
            if position == 0:
                newNode.next = self.head 
                self.head = newNode 
                
            # inserting at end 
            elif position == 1:
                self.tail.next = newNode 
                newNode.next = self.tail 
                
            # inserting at particular position
            else:
                tempNode = self.head 
                index = 0
                while index < position -1:
                    tempNode = tempNode.next 
                    index+=1
                nextNode = tempNode.next   
                tempNode.next = newNode
                newNode.next = nextNode 
                
    def traverse(self):
        if self.head is None:
            return "LL is Empty Please insert!!"
        else:
            node = self.head 
            while node is not None:
                print(node.value)
                node = node.next
                
    def search(self,target):
        if self.head is None:
            return "insert karo"
        else:
            node = self.head
            index = 0
            while node is not None:
                if node.value == target:
                    return ("yes",index)
                index+=1
                
            return "No"
        
    def delete(self,location):
        if self.head is None:
            return "LL is empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None 
                else:
                    self.head = self.head.next 
                    
            elif location == -1:
                if self.head == self.tail:
                    self.head = None 
                    self.tail = None 
                    
                else:
                    node = self.head 
                    while node is not None:
                        if node.next == None:
                            break 
                        node = node.next 
                    node.next = None
                    self.tail = node
                    
            else:
                tempNode = self.head 
                index = 0
                while index < location -1:
                    tempNode = tempNode.next 
                    index+=1
                nextNode = tempNode.next 
                tempNode.next = nextNode.next 
    def dele(self):
        self.head = None
        self.tail = None 
        
SLL = SinglyLikedList()    
SLL.insert(1, 0)
SLL.insert(2, 1)
SLL.insert(3, 2)
SLL.insert(4, 3)

SLL.insert(0, 0)
SLL.insert(0, 4) 

print([node.value for node in SLL])  
SLL.dele() 
print([node.value for node in SLL])  
                
                
            
            
    