# Python で WebServer

オライリー『入門 Python3』 の例を使用。

## HTTP server

p. 281

```sh
$ python -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/)
```

<http://localhost:8000> でアクセスできる。

0.0.0.0: 任意の TCP アドレス
127.0.0.1, localhost: クライアントの IP アドレス

## UDP server

p.356

以下、server を実行してから client 実行すると動く。

server: [`udp_server.py`](udp_server.py)
client: [`udp_client.py`](udp_client.py)

## TCP server

server: [`tcp_server.py`](tcp_server.py)
client: [`tcp_client.py`](tcp_client.py)

## RPC の実験

### XML-RPC

オライリー『入門 Python3』 p.371

server: [`xmlrpc_server.py`](xmlrpc_server.py)
client: [`xmlrpc_client.py`](xmlrpc_client.py)

### msgpack-RPC

```sh
pip install msgpack-rpc-python
```

server: [`msgpack_server.py`](msgpack_server.py)
client: [`msgpack_client.py`](msgpack_client.py)

### RPC

- JSON, XML
- MsgPack
- ProtocolBuffer
- FlatBuffer

## Reference

- [Google Developers Blog: Introducing gRPC, a new open source HTTP/2 RPC Framework](https://developers.googleblog.com/2015/02/introducing-grpc-new-open-source-http2.html)
- [FlatBuffers: FlatBuffers](http://google.github.io/flatbuffers/)


### Rebuild

- [Rebuild: 3: MessagePack (frsyuki, kiyoto)](http://rebuild.fm/3/)
- [Rebuild: 81: Enable The Broken Web (Hajime Morrita)](http://rebuild.fm/81/)
  - gRPC
- [Rebuild: 124: Universal Sushi (hak)](http://rebuild.fm/124/)
  - FlatBuffer
- [Rebuild: 45: Remembering WSDL (gfx)](http://rebuild.fm/45/)
- [Rebuild: 193: Winter Is Coming (gfx)](http://rebuild.fm/193/)
- [Rebuild: 99: The Next Generation Of HTTP (kazuho)](http://rebuild.fm/99/)
