#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import time

async def worker_1():
    print("worker_1 start")
    await asyncio.sleep(1)
    print("worker_1 done")

async def worker_2():
    print("worker_2 start")
    await asyncio.sleep(2)
    print("worker_2 done")

async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print("before wait")
    await task1
    print("awaited worker_1")
    await task2
    print("awatied worker_2")

time_start = time.time()
asyncio.run(main())
time_end = time.time()
print("Work time: {:.2f}".format(time_end - time_start))

"""
1. asyncio.run(main())，程序进入main()函数，事件开始循环
2. task1, task2任务同时被创建，并进入事件循环，等待执行,打印'before wait'
3. await task1执行，用户选择从主任务切出，调度器开始调度worker_1
4. 打印'worker_1 start', 运行到await asyncio.sleep(1)，从当前任务切出，开始调度worker_2
5. worker_2开始执行，打印'worker_2 start'，运行到await asyncio.sleep(2)， 从当前任务切出
6. 以上所有运行的事件，时间在1ms到10ms之间，事件调度器应该从这个时候开始调度
7. 一秒钟后，worker_1的sleep完成，事件调度器把控制权交给task1,输出'worker_1 done', task1任务完成，从事件循环中退出。
8. await task1任务完成，事件调度器把控制权交给主任务，打印'awaited worker_1',然后再await task2处继续处理


-------output---------
before wait
worker_1 start
worker_2 start
worker_1 done
awaited worker_1
worker_2 done
awaited worker_2
Work time 2.00
"""
