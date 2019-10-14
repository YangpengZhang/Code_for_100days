#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:50:05 2019

@author: zhangyangpeng
"""
import numpy as np
#%% exchange variable 
a, b = 5,10
print(a,b)
#%%
a , b = b, a
print(a,b)



#%%
a  = ['Python','is','awesome']
print(' '.join(a))

#%% most frequently element in a list
a = [1,2,3,4,3,3,3,3,4,4,4,4,1,11,1,1,1,1]
print(max(set(a),key=a.count))
'''using counter from collection'''
from collections import Counter
cnt = Counter(a)
print(cnt.most_common(9))

#%%check the lists are the same or not
from collections import Counter
str1 = 'hello world'
str2 = 'hello world'
Counter(str1) == Counter(str2)
 
#%% reversing string with special caseof slice step para
a = 'abcdefghijklmnopqrstuvwxyz'
print(a[::-1])
'''iterating over string contents in reverse efficiently'''
for char in reversed(a):
    print(char)
'''iterating an integer through type conversion and slicing'''
num = 1234567
print(int(str(num)[::-1]))
#%%reversing lists with special case of slice step para
a = [5,4,3,2,1]
print(a[::-1])
for ele in reversed(a):
    print(ele)

#%% transpose 2d array [[a,b],[c,d],[e,f]] -->[[a,c,e],[b,d,f]]
original = np.array([['a','b'],['c','d'],['e','f']])
transposed = zip(*original)
print(list(transposed))

#%%chained comparsion with all kind of operators
b = 6
print(4<b<7)
print(1==b<20)

#%% calling different functions with same arguments based on condition
def product(a,b):
    
    return a*b
def add(a,b):
    
    return a+b

b = False #由b的值判断是加还是乘
print((product if b else add)(5,7))

#%% a fast way to make a shallow copy of a list
a = [1,2,3,4,5]
b = a
b[0] = 10
print('a =%s  ,b =%s'%(a,b))
'''both a and b will be [10,2,3,4,5]'''
#%%
a = [1,2,3,4,5]
b = a[:]
b[0] = 10
print('a =%s  ,b =%s'%(a,b))
'''only b will change to [10,2,3,4,5]'''
#%%
'''copy  list by typecasting method'''
a = [1,2,3,4,5]
print(list(a))
'''using list.copy() method (python 3 only)'''
a = [1,2,3,4,5]
print(a.copy())
#%%
'''copy nested list using deepcopy'''
from copy import deepcopy
l = [[1,2],[3,4]]
l2 = deepcopy(l)
print(l2)
#%%
'''returning none or dedault value,when key is not in dictionary'''
d = {'a':1,'b':2}
print(d.get('c',3))
#%%
"""sorted a dictionary by its values with the built-in sorted() function and a 'key' argument"""
d = {'apple':1,'orange':2,'banana':5,'grapes':1}
print(sorted(d.items(),key=lambda x: x[1]))
'''sort using operator.itemgetter as the sort key instead of a lambda'''
from operator import itemgetter
print(sorted(d.items(),key=itemgetter(1)))
'''sort dict keys by value'''
print(sorted(d,key=d.get))

#%%
'''else gets called when for loop does not reach break statement'''
a = [1,2,3,4,5]
for ele in a:
    if ele==0:
        break
    else:
        print('did not break out of for loop')












    
