import socket

# 創建 Socket 物件
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 連接到伺服器
server_address = ('172.20.10.2', 8000)
client_socket.connect(server_address)

# 發送數據
message = input("The Fabonnaci(n) when n = ")
client_socket.send(message.encode())

data = client_socket.recv(1024)
print(f"the ans is {data.decode()}")

# 關閉連接
client_socket.close()
