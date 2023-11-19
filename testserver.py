import socket

HOST = '172.20.10.3'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(5)

print('Server started at: %s:%s' % (HOST, PORT))

while True:
    print('Waiting for connection...')
    conn, addr = server.accept()
    print('Connected by ' + str(addr))
    while True:
        indata = conn.recv(1024)
        if len(indata) == 0: # connection closed
            conn.close()
            print(str(addr) + ' closed connection')
            break

        inputdata = indata.decode()
        print(str(addr) + ': ' + inputdata)

        outdata = 'Echo: ' + indata.decode()
        conn.send(outdata.encode())