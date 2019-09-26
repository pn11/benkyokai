from xmlrpc.server import SimpleXMLRPCServer

def double(num):
    return num *2

def double_list(nums):
    return [num*2 for num in nums]

server = SimpleXMLRPCServer(("localhost", 6789))
server.register_function(double, "double")
server.register_function(double_list, "double_list")
print(server.get_request()[0].recvmsg)
server.serve_forever()
