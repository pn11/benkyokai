'''オライリー『入門Python3』 p.358'''
from datetime import datetime
import socket

address = ('localhost', 6789)
max_size = 4096

# AF_INET: IPソケットを作る, SOCK_STREAM: TCP, SOCK_DGRAM: UDP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5) # 5個まで接続できる

client, addr = server.accept()
print(f"Connected {client}, {address}")

data = client.recv(max_size)
print(f'Recieved from {client}: {data.decode("utf-8")}')
client.close()
server.close()
