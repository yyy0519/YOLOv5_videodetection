import socket
import struct
import main

def sent(data):
	 # 创建一个 TCP 客户端套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器的 IP 地址和端口号
    host = '123.249.122.15'
    port = 8000
    client_socket.connect((host, port))

    # # 读取图片文件
    # with open('voiceData.txt', 'rb') as f:
    #     data = f.read()

    # 发送图片数据长度到服务器
    size = len(data)
    packed_size = struct.pack('!I', size)
    client_socket.sendall(packed_size)

    # 发送图片数据到服务器
    client_socket.sendall(data)

    # 等待服务器响应
    response = client_socket.recv(1024)
    print(response)

    # 关闭客户端套接字
    client_socket.close()

if __name__ == '__main__':
    while True:
        TOTAL,mTOTAL,ActionCOUNTER,statu,action=main.GetData()
        my_list = [TOTAL, mTOTAL, ActionCOUNTER, statu, action]
        sent(my_list)        
