# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 18:55:32 2022

@author: Ashad Alam
"""

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None 
        self.prev = None 
        
class DoublyLL:
    def __init__(self):
        self.head = None 
        self.tail = None 
        
    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next 
    
    def create(self, nod):
        node = Node(nod)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        
    def insert(self, value, position):
        if self.head is None:
            return "LL is empty"
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
                index  = 0
                while index < position - 1:
                    tempNode = tempNode.next 
                    index += 1   
                nextNode = tempNode.next 
                newNode.next = nextNode 
                newNode.prev = tempNode 
                tempNode.next = newNode 
                nextNode.prev = newNode 
                
                
    def traversal(self):
        if self.head is None:
            return "LL is empty"
        else:
            node = self.head 
            while node:
                print(node.value)
                node = node.next 
    
    def reversal(self):
        if self.head is None:
            return "LL is empty"
        else:
            node = self.tail 
            while node:
                print(node.value)
                node = node.prev 
                
    def search(self,target):
        if self.head is None:
            return "LL is Empty"
        else:
            node = self.head 
            while node:
                if node.value == target:
                    return True
                node = node.next 
            return False 
        
    def delete(self, position):
        if self.head is None:
            return "LL is Empty"
        else:
            if position == 0:
                if self.head == self.tail:
                    self.head = None 
                    self.tail = None 
                else:
                    self.head = self.head.next
                    self.head.prev = None
                    
            elif position == 1:
                if self.head == self.tail:
                    self.head = None 
                    self.tail = None
                else:
                    self.tail = self.tail.prev 
                    self.tail.next = None 
                    
            else:
                curNode = self.head 
                index = 0
                while index < position - 1:
                    curNode = curNode.next 
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode 
        return "LL node is Delets"
    
    def DEL(self):
        if self.head is None:
            return "LL is EMpty"
        else:
            node = self.head 
            while node:
                node.prev = None 
                node = node.next
            self.head = None 
            self.tail = None
    
DLL = DoublyLL()
DLL.create(5)

DLL.insert(0,0)
DLL.insert(2,1)
DLL.insert(3,1)

print([node.value for node in DLL])
DLL.traversal()
print("")
DLL.reversal()

print(DLL.search(5))

DLL.delete(1)
print([node.value for node in DLL])

DLL.DEL()
print([node.value for node in DLL])             
                    
                
            