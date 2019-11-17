# _*_ coding : UTF-8 _*_
# 开发团队 ： Arthur
# 开发人员 ： arthur
# 开发时间 ： 2019/11/14 下午11:08
# 文件名称 ： thread_test.py
# 开发工具 ： PyCharm

import threading, time
def process():
    for i in range(3):
        time.sleep(1)
        print("thread name is {}".format(threading.current_thread().name))

if __name__ == "__main__":
    print("-----主线程开始------")
    threads = [threading.Thread(target=process) for i in range(4)]   #创建4个线程，存入列表
    for i in threads:
        i.start()

    for i in threads:
        i.join()

    print("------主线程结束------")
# 4个线程同时打印，总共各打印3次