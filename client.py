import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 2000))
print(client.recv(2048).decode('utf-8'))
try:
    while True:
        client.send(input('Enter text to server:\n').encode('utf-8'))
        data = client.recv(2048).decode('utf-8')
        time.sleep(3)

        if data == 'exit':
            print('>>>\nExit command recieved\nBye!\n<<<')
            client.shutdown(socket.SHUT_WR)
            exit()

        if data:
            print('\nData from server:')
            print(data, end='\n\n')
except KeyboardInterrupt:
    client.shutdown(socket.SHUT_WR)
