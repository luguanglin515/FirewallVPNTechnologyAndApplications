import socket
import sys
import time
sys.stdout.reconfigure(encoding='utf-8')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))
client.send('你好，服务器'.encode())
data = client.recv(1024)
print('收到：', data.decode())

# 让程序卡住30秒，不关闭连接
time.sleep(30)
client.close()