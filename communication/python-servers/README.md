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

server: `udp_server.py`(udp_server.py)
client: `udp_client.py`(udp_client.py)

## TCP server

## RPC の実験

- WebSocket
- JSON, XML
- MsgPack
- ProtocolBuffer
- FlatBuffer

### 分類

- 速度
- 分かりやすさ、使い勝手
- 普及率

### XML-RPC の例

オライリー『入門 Python3』 p.371
