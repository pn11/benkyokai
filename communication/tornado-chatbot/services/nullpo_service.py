from xmlrpc.server import SimpleXMLRPCServer

def nullpo():
    return "ガッ"

server = SimpleXMLRPCServer(("localhost", 20001))
server.register_function(nullpo, "nullpo")
print(server.get_request()[0].recvmsg)
server.serve_forever()
