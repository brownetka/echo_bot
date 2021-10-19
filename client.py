import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = int(input('Type here a number of port you want to connect (default is 2000)\n'))
name = input('Type here a hostname you want to connect (default is localhost)\n')
try:
    client.connect((name, port))
except (ConnectionRefusedError, socket.gaierror):
    print("Connection with this IP or port doesn't available now.\nWould like to set defaults? Y\\N")
    if input() == "Y":
        client.connect(('127.0.0.1', 2000))
    else:
        print('OK. Try again...')
        exit()
print(client.recv(2048).decode('utf-8'))
try:
        while True:
            client.send(input('Enter text to server:\n').encode('utf-8'))
            data = client.recv(2048).decode('utf-8')
            time.sleep(3)

            if data.lower() == 'exit':
                print('>>>\nExit command received\nBye!\n<<<')
                client.send('User disconnected\n'.encode('utf-8'))
                client.shutdown(socket.SHUT_WR)
                exit()

            if data:
                print('\nData from server:')
                print(data, end='\n\n')
except KeyboardInterrupt:
    client.shutdown(socket.SHUT_WR)
