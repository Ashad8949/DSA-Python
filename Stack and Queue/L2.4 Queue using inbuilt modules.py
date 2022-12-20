# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:44:56 2022

@author: Ashad Alam

Collection Dequeue
"""

from collections import deque

que = deque(maxlen=3) 
que.append(1)
que.append(2)
que.popleft()
print(que)

import queue as q 

que = q.Queue(maxsize = 3)
que.put(1)
que.put(2)
que.put(3)
print(que.qsize())
print(que.full())