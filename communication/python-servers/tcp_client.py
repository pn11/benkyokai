from datetime import datetime
import socket

server_address = ('localhost', 6789)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)
client.sendto(bytes('とぅっとぅるー', 'utf-8'), server_address)

client.close()
