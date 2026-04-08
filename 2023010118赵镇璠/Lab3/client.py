import socket
import sys
import time

# 解决中文乱码问题
sys.stdout.reconfigure(encoding='utf-8')

# 1. 创建TCP套接字
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 连接服务器（端口9999，与服务器一致）
client.connect(('127.0.0.1', 9999))
# 3. 发送数据
client.send('你好，服务器'.encode())
# 4. 接收响应
data = client.recv(1024)
print('收到：', data.decode())

# 5. 让程序卡住30秒，模拟长连接/不关闭连接（测试用）
time.sleep(30)

# 6. 关闭连接
client.close()