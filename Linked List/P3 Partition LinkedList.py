# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 20:29:41 2022

@author: Ashad Alam
"""

from LinkedList import LinkedList 

def Partition(ll, x):
    curNode = ll.head 
    ll.tail = ll.head 
    
    while curNode:
        nextNode = curNode.next 
        curNode.next = None 
        if curNode.value < x:
            curNode.next = ll.head 
            ll.head = curNode 
        else:
            ll.tail.next = curNode 
            ll.tail = curNode 
        curNode = nextNode 

ll = LinkedList()
ll.generate(10, 10, 99)
print(ll)
print(Partition(ll, 50))
print(ll)          
    
    
    