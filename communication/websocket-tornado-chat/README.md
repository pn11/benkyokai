# Chat on Tornado

Copied from [Tornado's official demo](https://github.com/tornadoweb/tornado/tree/stable/demos/websocket).

## Usage

```sh
python3 chatdemo.py
```

and open <http://localhost:8888>.

### Connect via WebSocket

```sh
yarn global add wscat
wscat -c localhost:8888.chatsocket
```

```wscat
>{"body": "Hello"}
```
