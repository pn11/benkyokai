from datetime import datetime
import socket

server_address = ('localhost', 6789)
max_size = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

data, client = server.recvfrom(max_size)
print(f'Recieved from {client}: {data.decode("utf-8")}')

server.close()
