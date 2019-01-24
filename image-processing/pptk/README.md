# pptk

- [Qiita記事](https://qiita.com/pn11/items/dfe2b7baf4a3741206dd) を書いた。

pptk は手軽に点群を表示できる Python ライブラリ。

- [heremaps/pptk: The Point Processing Toolkit (pptk) is a Python package for visualizing and processing 2-d/3-d point clouds.](https://github.com/heremaps/pptk)

## 導入

```
pip install pptk
```

で入る。

## Ubuntu 18.04 での注意

Ubuntu 18.04 の場合は以下の対応が必要。

- [pip install pptk doesn't work on ubuntu 18.04/kubuntu 18.04 · Issue #3 · heremaps/pptk](https://github.com/heremaps/pptk/issues/3#issue-369762268)

virtualenv の場合は以下のようになる。

```bash
cd venv/lib/python3.6/site-packages/pptk/libs/
mv libz.so.1 libz.so.1.old
ln -s /lib/x86_64-linux-gnu/libz.so.1
```
