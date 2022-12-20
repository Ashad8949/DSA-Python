# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 22:36:56 2022

@author: Ashad Alam
"""
from LinkedList import LinkedList

def Sum(la, lb):
    n1 = la.head 
    n2 = lb.head 
    carry = 0
    ll = LinkedList()
    while n1:
        if n1:
            result = n1.value + n2.value + carry
            rem = (result%10)
            ll.add(rem)
            carry = result//10 
            n1 = n1.next 
            n2 = n2.next 
    if carry:
        ll.add(carry)
        return ll
            
    return ll 

la = LinkedList()
la.add(9)
la.add(3)
la.add(8)

print("la",la)

lb = LinkedList()
lb.add(8)
lb.add(3)
lb.add(7)
print("lb",lb)

print('ll',Sum(la,lb))