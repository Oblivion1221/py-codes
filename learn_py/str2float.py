# -*- coding: utf-8 -*-
from functools import reduce
def str2float(s):
    i = 1
    def char2f(s):
        return {'0':0, '1':1, '2':2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    while s[i] != '.':
        r1 = reduce(lambda x, y: x*10+y, map(char2f, s[:i+1]))
        i += 1
    r2 = reduce(lambda x, y: x*10+y, map(char2f, s[i+1:]))/10**len(s[i+1:])
    return r1 + r2

print('str2float(\'123.456\') =', str2float('123.456'))
        
            
