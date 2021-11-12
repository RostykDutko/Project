import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
IP = socket.gethostbyname(socket.gethostname())
PORT = 12333
listener.bind((IP, PORT))
listener.listen(0)
connection, address = listener.accept()

connection.send("hi , go here".encode('utf8'))

while True:
    data_encode = ''
    while True:
        data = connection.recv(1024).decode('utf8')
        data_encode += data
        print(data)
        message = input("Enter a message: ")
        connection.send(message.encode('utf8'))
        if not data: 
            break