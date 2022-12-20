# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 18:01:11 2022

@author: Ashad Alam
"""

class Node:
    def __init__(self,value = None):
        self.value = value 
        self.next = None 
        self.prev = None 
        
class CircularDLL:
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
        self.head = node 
        self.tail = node 
        node.next = node 
        node.prev = node
        return "Node created Successfully"
    
    def insert(self, value, position):
        if self.head is None:
            return "LL is empty"
        else:
            newNode = Node(value)
            if position == 0:
                newNode.next = self.head 
                newNode.prev = self.tail
                self.head.prev = newNode 
                self.tail.next = newNode 
                self.head = newNode
                
            elif position == 1:
                newNode.next = self.head 
                newNode.prev = self.tail 
                self.tail.next = newNode 
                self.head.prev = newNode 
                self.tail = newNode
                
            else:
                tempNode = self.head 
                index = 0
                while index < position - 1:
                    tempNode = temNode.next 
                    index += 1
                newNode.next = tempNode.next 
                newNode.prev = tempNode 
                tempNode.next.prev = newNode 
                tempNode.next = newNode 
                
    def traversal(self):
        if self.head is None:
            return "LL is empty"
        else:
            node = self.head 
            while node:
                print(node.value)
                node = node.next
                if node == self.tail.next:
                    break
                
    def reversal(self):
        if self.head is None:
            return "LL is empty"
        else:
            node = self.tail
            while node:
                print(node.value)
                node = node.prev
                if node == self.head.prev:
                    break
                
    def search(self, target):
        if self.head is None:
            return ["LL is empty",-1]
        else:
            node = self.head 
            index = 0
            while node:
                if node.value == target:
                    return [True,index]
                node = node.next
                index += 1
                if node == self.tail.next:
                    break
        return [False]
    
    def delete(self,position):
        if self.head is None:
            return "LL is Empty"
        else:
            if position == 0:
                if self.head == self.tail:
                    node = self.head 
                    node.next = None 
                    node.prev = None 
                    self.head = None 
                    self.tail = None 
                    
                else:
                    self.head = self.head.next 
                    self.tail.next = self.head 
                    self.head.prev = self.tail 
                    
            elif position == 1:
                if self.head == self.tail:
                    node = self.head 
                    self.head.next = None 
                    self.head.prev = None 
                    self.head = None 
                    self.tail = None
                    
                else:
                    self.tail = self.tail.prev 
                    self.head.prev = self.tail 
                    self.tail.next = self.head 
                    
            else:
                node = self.head 
                index = 0
                while index<position - 1:
                    node = node.next 
                    index += 1
                node.next.next.prev = node 
                node.next = node.next.next
                
    def DEL(self):
        node = self.head 
        while node:
            node.prev = None 
            node = node.next 
            if node == self.tail.next:
                break
        self.head = None 
        self.tail = None 
        
CDLL = CircularDLL()
print(CDLL.create(5))
CDLL.insert(1,0)
CDLL.insert(6,1)
CDLL.insert(3,-1)
print([node.value for node in CDLL])
CDLL.traversal()
print("---***---")
CDLL.reversal()
print(CDLL.search(6))
print(CDLL.search(0))

CDLL.delete(-1)
print([node.value for node in CDLL])

CDLL.DEL()
print([node.value for node in CDLL])