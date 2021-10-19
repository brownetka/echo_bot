import socket
import time
print('Starting server...')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2000))

try:
    server.listen(1)
    print('Server is listening')

    client_socket, address = server.accept()
    print(f'User with ip {address} connected')

    client_socket.send('You are connected!'.encode('utf-8'))
    while True:
        try:
            data = client_socket.recv(2048).decode('utf-8')
        except OSError:
            data = None

        time.sleep(3)
        if data:
            print('\nReceiving data from client:')
            print(data)

        client_socket.send(input('\nEnter text to client:\n').encode('utf-8'))
except KeyboardInterrupt:
    print('Server is shutting down')
    server.shutdown(socket.SHUT_WR)
