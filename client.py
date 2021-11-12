import socket

connection = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
IP = '192.168.0.196'
PORT = 12333
connection.connect((IP, PORT))
rd = connection.recv(1024)
print(rd.decode('utf8'))
connection.send("Hi for you too ".encode('utf8'))

while True:
    data_encode = ''
    while True:
        data = connection.recv(1024).decode('utf8')
        print(data)

        connection.send(input("Enter code").encode('utf8'))
