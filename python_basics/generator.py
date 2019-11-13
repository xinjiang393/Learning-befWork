#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
1. 生成器就是一个懒人版的迭代器
2. [i for i in range(100000000)]生成一个一亿元素的列表 ，每个元素都会存在于内存中。
3. 但是我们不需要同时在内存中保存这么多东西，比如求和，只要知道相加那一刻是多少就行，用完就扔掉。
4. 所以生成器就是调用了next()函数后才会生成下一个变量。生成器用小括号： (i for i range(100000000))
5. 生成器在初始化的时候，并不需要运行一次生成操作，所以test_generator()节省了一亿次生成操作。
"""

import os
import psutil

def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)
    info = p.memory_info()
    memory = info.rss / 1024. / 1024.
    print("{} memory used: {}".format(hint, memory))

def test_iterator():
    show_memory_info("initing interator")
    list_1 = [i for i in range(100000000)]
    show_memory_info("after iterator initiated")
    print(sum(list_1))
    show_memory_info("after sum called")

def test_generator():
    show_memory_info("initing generator")
    list_2 = (i for i in range(100000000))
    show_memory_info("after generator initiated")
    print(sum(list_2))
    show_memory_info("after sum called")

test_iterator()
test_generator()
