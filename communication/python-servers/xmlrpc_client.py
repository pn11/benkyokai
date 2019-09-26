import xmlrpc.client
import datetime

proxy = xmlrpc.client.ServerProxy("http://localhost:6789")
num = 7
print(datetime.datetime.now())
result = proxy.double(num)
nums = [float(i) for i in range(100000)]
result = proxy.double_list(nums)
print(datetime.datetime.now())
#print(f"Double {num} is {result}")
