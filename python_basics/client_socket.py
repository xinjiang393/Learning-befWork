# _*_ coding : UTF-8 _*_
# 开发团队 ： Arthur
# 开发人员 ： arthur
# 开发时间 ： 2019/11/17 下午8:05
# 文件名称 ： client_socket.py
# 开发工具 ： PyCharm

import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))
print("已建立连接")
info = ""
while info != "byebye":
    send_data = input("输入发送内容： ")
    s.send(send_data.encode())       # 发送TCP数据流
    if send_data == "byebye":
        break
    info = s.recv(1024).decode()     # recive message from remote server
    print("接收到的内容： " + info)
s.close()