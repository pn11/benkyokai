from datetime import datetime
import socket

server_address = ('localhost', 6789)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'hey', server_address)

client.close()
