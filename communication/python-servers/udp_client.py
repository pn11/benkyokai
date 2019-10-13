from datetime import datetime
import socket

server_address = ('localhost', 6789)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(bytes('牧瀬紅莉栖が、何者かに刺されたみたいだ・・・', 'utf-8'), server_address)

client.close()
