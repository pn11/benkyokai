import datetime
from msgpackrpc import Client, Address

client = Client(Address("localhost", 6789))
num = 8
print(datetime.datetime.now())
result = client.call('double', num)
nums = [float(i) for i in range(100000)]
result = client.call('double_list', nums)
print(datetime.datetime.now())
#print(f"Double {num} is {result}")
