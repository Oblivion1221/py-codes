# -*- coding: utf-8 -*-

def triangles():
    t = [1]
    while True:
        yield t
        t = [1] + [t[i]+t[i+1] for i in range(len(t)-1)] + [1]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break