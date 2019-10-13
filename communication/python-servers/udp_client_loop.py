from datetime import datetime
import socket

server_address = ('localhost', 6789)

t1 = datetime.now()

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(10000):
    client.sendto(bytes(f'{i}', 'utf-8'), server_address)
client.close()
t2 = datetime.now()
print(t2-t1)
