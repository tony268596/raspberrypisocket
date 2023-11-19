import socket

# 建立 Socket 物件
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '172.20.10.3'
port = 8000

# 綁定主機和端口
server_socket.bind((host, port))


# 開始監聽連接
server_socket.listen(5)

def fabonnaci(n):
    if n==0 or n==1:
        return n
    ret = [0,1]
    for _ in range(n-1):
        ret.append(ret[-1]+ret[-2])
    return ret[-1]


if __name__ == "__main__":
    while True:
        print("Waiting for connection...")

        # 接受連接
        client_socket, addr = server_socket.accept()
        print(f"Add connection from {addr}")

        # 接收數據
        data = client_socket.recv(1024)
        print(f"Received from {addr}: {data.decode()}")
        try:
            response = str(fabonnaci(int(data)))
        except ValueError:
            print("conection closed")
            break
        print(f"Send to {addr}: {response}")
        client_socket.send(response.encode())

        # 關閉連接
        print("conection closed")
        client_socket.close()



