import socket


def main():
    # >>1. 创建客户端的socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # >>2. 连接上服务器
    address = ("127.0.0.1", 8000)
    client.connect(address)
    # >>3. 向服务器发送数据
    msg = input("请输入向服务器端发送的数据:")
    client.send(msg.encode())
    # >>4. 接收服务器的数据
    data = client.recv(1024)
    print("服务器的数据:", data.decode())
    # >>5. 关闭客户端
    client.close()


if __name__ == "__main__":
    main()
