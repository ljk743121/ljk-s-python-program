import socket  # 导入包


def udp_socket():
    # 创建udp套接字,socket.socket()中传入两个参数，第一个为ip类型协议（socket.AF_IENT指的是ipv4协议），第二个时传输协议（这里指的是udp协议）
    u_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        # 发送数据
        send_data = input("请输入要发送的数据:")
        if send_data == "exit":  # 如果输入字符串是exit，程序退出
            break
        address = ("192.168.1.107",9999) # 目的IP地址和端口号, ip地址为字符串类型，而端口号为int类型
        u_socket.sendto(send_data.encode('utf-8'), address)  # 在发送时，要将发送的内容进行编码，以字节的方式传输

    u_socket.close()  # 关闭套接字


if __name__ == "__main__":
    udp_socket()
