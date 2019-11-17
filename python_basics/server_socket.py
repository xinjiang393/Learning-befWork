# _*_ coding : UTF-8 _*_
# 开发团队 ： Arthur
# 开发人员 ： arthur
# 开发时间 ： 2019/11/17 下午8:00
# 文件名称 ： server_socket.py
# 开发工具 ： PyCharm
import socket

host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
sock, addr = s.accept()
print("连接已建立")
info = sock.recv(1024).decode()
while info != "byebye":
    if info:
        print("接收到的内容： " + info)
    send_data = input("输入发送内容：")
    sock.send(send_data.encode())
    if send_data == "byebye":
        break
    info = sock.recv(1024).decode()
sock.close()
s.close()

