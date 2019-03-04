#Craps Roller
#演示随机数的生成
#如果确实需要用到真正的随机数，访问http://www.fourmilab.ch/hotbits/.
#该网站是根据不可预测的自然放射性衰变过程来生成随机数的。

import random
pie1 = random.randint(1, 6)   ##生成的随机数范围[1，2，3，4，5，6]
pie2 = random.range(6) + 1    ##生成的随机数范围[0，1，2，3，4，5]
#pie1与pie2生成随机数是一样的，只是表现方式不同

total = pie1 + pie2

print("You rolled a ", pie1, "and a", pie2, "for a total of", total)

input("\n\nPress the enter key to exit.")
