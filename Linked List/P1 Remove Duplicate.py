# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 13:00:24 2022

@author: Ashad Alam

Prob: Remove Duplicate from Linked List

"""

from LinkedList import LinkedList 

def removeDuplicate(ll):
    if ll.head is None:
        return 
    else:
        node = ll.head 
        visited = set([node.value])
        while node.next:
            if node.next.value in visited:
                node.next = node.next.next 
            else:
                visited.add(node.next.value)
                node = node.next 
                
        return ll
    
custumLL = LinkedList()
custumLL.generate(6, 0, 10)
print(custumLL)
removeDuplicate(custumLL)
print(custumLL)
