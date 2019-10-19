# Chatbot system with Tornado and XML-RPC

WebSocket server is copied from [Tornado's official demo](https://github.com/tornadoweb/tornado/tree/stable/demos/websocket).

## Usage

### Start services

```sh
cd services
python3 calc_service.py
python3 nullpo_service.py
```

### Start websocket server

```sh
python3 chatdemo.py
```

and open <http://localhost:8888>.

### Connect via WebSocket

```sh
yarn global add wscat
wscat -c localhost:8888/chatsocket
```

```wscat
>{"body": "Hello"}
```
