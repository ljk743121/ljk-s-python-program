import socket


def recv_data():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_adress = ("", 9999)  # 类型为元组，绑定本地信息,在绑定本地信息时,ip地址可以不用写
    udp_socket.bind(local_adress)  # 必须绑定自己电脑的ip以及port，其他的不行
    print("正在接收数据...")
    while True:  # 循环接收数据
        # 接收数据
        data = udp_socket.recvfrom(1024)  # 最大支持接收1024个字节
        content = data[0]  # 发送的内容
        if content.decode("gbk") == "exit":  # 当收到数据为exit时，程序退出
            break
        send_address = data[1]  # 发送方IP地址和端口号
        # 为什么解码方式为gbk，因为在windows中默认的解码方式为gbk，所以utf-8不能识别，但在其他操作系统中使用utf-8进行解码
        print("%s发送：%s" % (str(send_address), content.decode("gbk")))

    udp_socket.close()  # 关闭套接字


if __name__ == '__main__':
    recv_data()
