# _*_ coding : UTF-8 _*_
# 开发团队 ： Arthur
# 开发人员 ： arthur
# 开发时间 ： 2019/11/13 下午10:44
# 文件名称 ： processes.py
# 开发工具 ： PyCharm

from multiprocessing import Process
import time
import os

def child_1(interval):
    print("子进程{}开始执行， 父进程{}".format(os.getpid(), os.getppid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("子进程{}执行时间{:0.2f}".format(os.getpid(), t_end - t_start))

def child_2(interval):
    print("子进程{}开始执行，父进程为{}".format(os.getpid(), os.getppid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("子进程{}执行时间{:0.2f}".format(os.getpid(), t_end - t_start))


if __name__ == '__main__':
    print("-----------父进程开始执行-------------")
    print('父进程PID：{}'.format(os.getpid()))
    p1 = Process(target=child_1, args=(1,))
    p2 = Process(target=child_2, name='mrsort', args=(2,))
    p1.start()
    p2.start()
    # 同时父进程仍然往下执行，如果P2进程还在执行，将会返回True
    print("p1.is_alive={}".format(p1.is_alive()))
    print("p2.is_alive={}".format(p2.is_alive()))
    #输出p1和p2进程的别名和PID
    print("p1.name = {}".format(p1.name))
    print("p1.pid = {}".format(p1.pid))
    print("p2.name = {}".format(p2.name))
    print("p2.pid = {}".format(p2.pid))
    print("---------waiting children process-------")
    p1.join()           #p1.join()是等到P1进程结束
    p2.join()
    print("---------父进程执行结束----------")
"""
1. 多进程与协程的区别，协程可以同时经常，包含上下文切换，但是多进程必须等上一个进程执行完毕
"""