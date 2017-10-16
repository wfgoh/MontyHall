# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 20:53:58 2017

@author: Christopher
"""

import numpy as np

samplesize = 100000
count1 = 0
count2 = 0
count3 = 0

for i in range(samplesize):
    rand = np.random.choice([1,2,3])
    if rand == 1:
        count1 += 1
    if rand == 2:
        count2 += 1
    if rand == 3:
        count3 += 1
        
print('Tot 1 = ',count1,', Prob = ',count1/samplesize)
print('Tot 2 = ',count2,', Prob = ',count2/samplesize)
print('Tot 3 = ',count3,', Prob = ',count3/samplesize)