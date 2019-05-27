# Tornado で WebSocket server を立てるサンプル

送ったものをおうむ返しするだけの WebSocket サーバーを Tornado で立てる。

## 依存モジュール

サーバーに tornado, クライアントに websockets を使う。

```bash
pip install tornado websockets
```

または

```bash
pip install -r requirements.txt
```

## 使い方

```bash
python server.py
```

でサーバーが起動。

```bash
python client.py
```

で WebSocket 接続をつくって、メッセージを送る。

## Simple WebSocket Client を使う

WebSocket サーバーにつなぐ時に、Chrome Extension の Simple WebSocket Client が便利。これからの接続を許可しているのが `server.py` の以下の部分。

```python
    def check_origin(self, origin):
        allowed = ["chrome-extension://pfdhoblngboilpfeibdedpjgfnlcodoo"]
        print(origin)
        if origin in allowed:
            print("Allowed connection from {}".format(origin))
            return True
        else:
            print("Blocked connection from {}".format(origin))
```
