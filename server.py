import socket
import time
print('Starting server...')
PORT = 2000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', PORT))

try:
    while True:
        server.listen(1)

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
            msg = input('\nEnter text to client:\n').encode('utf-8')
            client_socket.send(msg)
            if msg == 'exit'.encode('utf-8'):
                time.sleep(2)
                print('exit command found')
                server.shutdown(socket.SHUT_WR)
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                server.bind(('127.0.0.1', 2000))
                break
except KeyboardInterrupt:
    print('Server is shutting down')
    server.shutdown(socket.SHUT_WR)
except BrokenPipeError:
    print('Server doesnt have active users...\nShutting down!')
    server.shutdown(socket.SHUT_WR)