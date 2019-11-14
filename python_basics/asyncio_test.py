#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
1. 通过await()来调用，程序会阻塞在这里，进入被调用的协程函数，执行完毕后再继续。
2. asyncio.create_task()来创建任务
3. asyncio.run()来触发运行，一个非常好的编程规范，asyncio.run(main())作为主函数入口，在程序运行周期内，只调用一次asyncio.run。
4. asyncio.create_task()创建任务后很快被调度执行，而不会阻塞在任务队列这里。
5. 等待所有任务运行结束，用for task in tasks: await task即可
6. for  task。。。这条语句，可以改写成： awai asyncio.gather(*tasks),将列表变成函数参数
"""

import asyncio
import time

async def crawl_page(url):
    print("crawling {}".format(url)
    sleep_time = int(url.split("_")[-1])
    await asyncio.sleep(sleep_time)
    print("OK {}".format(url))

async def main(urls):
    tasks = [asyncio.create_tasks(crawl_page(url)) for task in tasks]
    await asyncio.gather(*tasks)

time_start = time.time()
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
time_end = time.time()
print("Wall time: {:.2f}".format(time_start - time_end))

"""
--------output---------
crawling url_1
crawling url_2
crawling url_3
crawling url_4
OK url_1
OK url_2
OK url_3
OK url_4
Wall time 4.00
"""

