# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 20:11:43 2022

@author: Ashad Alam
"""

from LinkedList import LinkedList 

def nthToLast(ll, n):
    p1 = ll.head 
    p2 = ll.head  
    
    for i in range(n):
        if p2 is None:
            return None 
        p2 = p2.next 
        
    while p2:
        p1 = p1.next
        p2 = p2.next 
    return p1 
    
ll = LinkedList()
ll.generate(10, 0 ,99)
print(ll)
print(nthToLast(ll, 3))