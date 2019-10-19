from xmlrpc.server import SimpleXMLRPCServer

def calc(expression):
    try:
        ret = str(eval(expression))
    except:
        ret = "Failed."
    return ret

server = SimpleXMLRPCServer(("localhost", 20002))
server.register_function(calc, "calc")
print(server.get_request()[0].recvmsg)
server.serve_forever()
