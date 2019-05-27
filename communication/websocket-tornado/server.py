import tornado
import tornado.websocket

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")
    
    def check_origin(self, origin):
        allowed = ["chrome-extension://pfdhoblngboilpfeibdedpjgfnlcodoo"]
        print(origin)
        if origin in allowed:
            print("Allowed connection from {}".format(origin))
            return True
        else:
            print("Blocked connection from {}".format(origin))

if __name__ == "__main__":
    app = tornado.web.Application([
        (r'/socket', EchoWebSocket),
    ])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()    

