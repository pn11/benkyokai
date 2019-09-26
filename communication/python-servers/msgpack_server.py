from msgpackrpc import Server, Address

class Services():
    def double(self, num):
        return num * 2
    
    def double_list(self, nums):
        return [num*2 for num in nums]
    
server = Server(Services())
server.listen(Address("localhost", 6789))
server.start()
