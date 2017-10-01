#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 17:29:54 2016

@author: Dovla
"""

import sys
import numpy as np
import IDlibtest1 as mylib


a = len(sys.argv)
b = str(sys.argv)
#print(a,b)

bagsLength = []
jacResults = []
i = 1
for i in range(a):
    firstWc = mylib.wordcount(sys.argv[i])
    firstBag = mylib.bag(firstWc, treshold=200)
    bagsLength.append(len(firstWc))
    ii = 1
    for ii in range(a):
        secondWc = mylib.wordcount(sys.argv[ii])
        secondBag = mylib.bag(secondWc, treshold=200)
        jacResults.append(1-mylib.jaccard(set(firstBag),set(secondBag)))
        #print(jacResults)	
        if ii > a:
            break
        else:
            ii = ii + 1
    
    if i > a:
        break
    else:
        i = i + 1

