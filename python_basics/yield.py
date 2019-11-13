#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
1. 生成器就是一个懒人版的迭代器
2. [i for i in range(100000000)]生成一个一亿元素的列表 ，每个元素都会存在于内存中。
3. 但是我们不需要同时在内存中保存这么多东西，比如求和，只要知道相加那一刻是多少就行，用完就扔掉。
4. 所以生成器就是调用了next()函数后才会生成下一个变量。生成器用小括号： (i for i range(100000000))
5. 生成器在初始化的时候，并不需要运行一次生成操作，所以test_generator()节省了一亿次生成操作。
"""

def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1

gen_1 = generator(1)
gen_3 = generator(3)
print(gen_1)
print(gen_3)

def get_sum(n):
    sum_1,sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print("next_1 = {}, next_3 = {}".format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)

get_sum(8)
"""
------------output-----------
<generator object generator at 0x00000000021D37D8>
<generator object generator at 0x00000000021FD830>
next_1 = 1, next_3 = 1
next_1 = 2, next_3 = 8
next_1 = 3, next_3 = 27
next_1 = 4, next_3 = 64
next_1 = 5, next_3 = 125
next_1 = 6, next_3 = 216
next_1 = 7, next_3 = 343
next_1 = 8, next_3 = 512
1296 1296
"""

