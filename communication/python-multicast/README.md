# UDP Multicast and Brodcast with Python

UDP でマルチキャストとブロードキャストで送信、受信を試す。  
Python の標準ライブラリを使用するので公式のドキュメントが一番良い参考資料。

- [socket --- 低水準ネットワークインターフェース — Python 3.8.4 ドキュメント](https://docs.python.org/ja/3/library/socket.html)
- [ソケットプログラミング HOWTO — Python 3.8.4 ドキュメント](https://docs.python.org/ja/3/howto/sockets.html)
- `socket.socket()` の引数については以下の表も参照。
  - [ソケット (BSD) - Wikipedia](https://ja.wikipedia.org/wiki/%E3%82%BD%E3%82%B1%E3%83%83%E3%83%88_(BSD)#BSD%E3%82%BD%E3%82%B1%E3%83%83%E3%83%88%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%95%E3%82%A7%E3%83%BC%E3%82%B9)

## Usage

### Receiver

```sh
python3 receiver.py 224.3.29.71 5000
```

### Transmitter

```sh
python3 transmitter.py 224.3.29.71 5000 hello
```
