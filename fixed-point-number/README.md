# Practice of fixed point numbers

## 内容

固定小数点演算を試してみた。掛け算とかだとすぐ桁落ちしてしまいそうなので、とりあえず足し算だけやってみた。

## How to build

First, CMake is needed.

```
cd build
cmake ..
```

Then,  
For Linux and Mac:

```
make
```

For Windows:  
Open `fixed-point-number.sln` and build.

## Reference

- [hdLab ： 第10回「固定小数点の演算」（201302） ～ 21世紀のシステムLSI設計を支援する　プロダクト＆サービス](http://www.hdlab.co.jp/web/a060onepoint/201302.php)
    - 図がきれいで分かりやすい。
- [固定小数点演算について](http://azsky2.html.xdomain.jp/note/paintprog/004_fixedarith.html)
- ["B"-con - Laboratory - Data & Algorithm - 固定小数点](http://www2s.biglobe.ne.jp/~nuts/labo/daal/daal07.html)
- [Play Stationにおける処理高速化と画像処理への応用 (PDF)](http://www-sens.sys.es.osaka-u.ac.jp/wakate/tutorial/group2/fixed_pn.pdf)