#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
1. 所有容器都是可迭代的，迭代器(iterable)提供了一个next方法，要么得到下一个对象，要么得到一个StopIteration的错误
2. 而可迭代对象，通过iter()函数返回一个迭代器，再通过next()函数就可以实现遍历。for in 语句只是将这个过程隐式化。

----------------------------------------
>>> iter(123)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'int' object is not iterable
----------------------------------------
"""

def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False

params = [
        1234,
        "1234",
        [1, 2, 3, 4],
        set([1, 2, 3, 4]),
        {1:1, 2:2, 3:3, 4:4},
        (1, 2, 3, 4)
        ]

for param in params:
    print("{} is iterable? {}".format(param, is_iterable(param)))

"""
---------------output--------------
1234 is iterable? False
1234 is iterable? True
[1, 2, 3, 4] is iterable? True
{1, 2, 3, 4, 5} is iterable? True
{1: 1, 2: 2, 3: 3, 4: 4} is iterable? True
(1, 2, 3, 4) is iterable? True
"""
