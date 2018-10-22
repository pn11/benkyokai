# ソケット通信のサンプル

こちらを参考に、スマートポインタとか使って少し C++ ぽく書き換えた。

- [Turbolinux｜ソリューション＆サービス](http://www.turbolinux.com/solution_service/library/features/c_magazine/vol_11.html)

## 使い方

```bash
mkdir build
cd build
cmake ..
make
```

でビルドする。ターミナルを立ち上げて

```
./socket_server
```

を実行するとサーバーが立ち上がる。別のターミナルを立ち上げて

```
./socket_client localhost
```

とするとサーバーからメッセージを受け取る。別のマシンからつなげる場合はポートを開放した上で、

```
./socket_client サーバーのアドレス
```

とすれば動くはず。
