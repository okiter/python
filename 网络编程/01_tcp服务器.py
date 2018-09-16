import socket


def main():
    # >>1. 创建服务器的socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # >>2. 绑定IP和端口号
    address = ("", 8000)
    server.bind(address)
    # >>3. 设置建立客户端的数量
    server.listen(124)
    # >>4. 获取连接的客户端的scoket和IP地址
    while 1:
        print("等待客户端的连接\n")
        client, client_ip = server.accept()
        print("客户端IP:", client_ip, "连接到服务器上")
        # >>5. 接收客户端的数据
        data = client.recv(1024)
        print("客户端的数据:", data.decode())
        # >>6. 向客户端发送收据
        client.send("服务器发送给客户端的数据\n".encode())
        # >>7. 关闭客户端连接
        client.close()
    # >>8. 关闭服务器不接收任何客户端的连接
    server.close()


if __name__ == "__main__":
    main()


"""
注意事项:
1. 通过accept获取的到的客户端.通过客户端和远程的客户端交互
"""