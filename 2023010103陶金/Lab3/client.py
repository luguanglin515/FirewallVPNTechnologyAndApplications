import socket
from time import sleep

# 阶段 1：创建套接字
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 阶段 2：连接服务器
client.connect(('192.168.35.141', 8080))

sleep(20)   # 等待

# 阶段 3：发送数据
client.send('你好，服务器'.encode())

# 阶段 3：接收响应
data = client.recv(1024)
print('收到：', data.decode())

# 阶段 4：断开
client.close()