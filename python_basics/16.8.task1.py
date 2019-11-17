# _*_ coding : UTF-8 _*_
# 开发团队 ： Arthur
# 开发人员 ： arthur
# 开发时间 ： 2019/11/17 下午3:37
# 文件名称 ： 16.8.task1.py
# 开发工具 ： PyCharm
"""
1. 输出信息中，如果有一一对应的条目，可以采用字典的形式，方便遍历打印
2. 现在是四个条目，开启四个进程。如果这种条目成千上万个，也开启这么多个进程，会导致内存暴增。
    因此，需要考虑开启N个进程，执行一遍后sleep，再继续执行下一批
"""

from datetime import datetime
from multiprocessing import Process

def delta(item, future):
    delta = datetime(*future) - datetime.now()
    print("{}还有:{:>20d}天".format(item, delta.days))

dict_items = {
    "2020高考": (2020, 6, 7),
    "东京奥运会": (2020, 7, 24),
    "北京冬奥会": (2022, 2, 4),
    "卡塔尔世界杯": (2022, 11, 21)
}

def main_head():
    datenow = datetime.now()
    y = datenow.year
    m = datenow.month
    d = datenow.day
    print("                       Today")
    print("            {} 年 {} 月 {} 日".format(y, m, d))
    print("距离:")



if __name__ == "__main__":
    main_head()
    # 如果需要显示的条目成千上万，那么列表推倒式会占用很大的内存。开启的进程也会是成千上万，更占内存
    # 所以，需要考虑一次遍历其中的部分条目。但是需要考虑，多次开启、停止进程占用的开销
    plist = [Process(target=delta, args=(key, value)) for key, value in dict_items.items()]
    for p in plist:
        p.start()           #p.start()return is None

    for p in plist:
        p.join()
