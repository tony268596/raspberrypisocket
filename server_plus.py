import socket
import threading

def handle_client(client_socket, address):
    print(f"Add connection from {address}")

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"[{address}] {data.decode()}")
            client_socket.send(f"收到: {data.decode()}".encode())
        except KeyboardInterrupt:
            client_socket.close()
            break
    print("conection closed")
    client_socket.close()



if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('172.20.10.3', 8000))
    server_socket.listen(5)

    print("Waiting for connection...")

    while True:
        try:
            client, address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client, address))
            client_thread.start()
        except KeyboardInterrupt:
            break
            