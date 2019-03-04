# Template Matching with Julia

## Installing Julia 1.0.3 on Ubuntu 18.04

```
wget https://julialang-s3.julialang.org/bin/linux/x64/1.0/julia-1.0.3-linux-x86_64.tar.gz
dtrx julia-1.0.3-linux-x86_64.tar.gz
```

## Packages

```julia
pkg> add Images
pkg> add ImageMagick
pkg> add ImageView
pkg> add TestImages # テスト用画像が入っている
```

## Image Sample

```
wget https://tvm.ai/images/rocm/cat.png
```


## Reference

### 環境構築

- [julia 0.6からjulia 1.0への移行 - Qiita](https://qiita.com/Hidekazu-Karino/items/eeda08fbd6f16c735843)
  - Julia 1.0 での python-venv 的なものの作り方

### JuliaImages

- [Juliaの画像処理ライブラリを使ってわかったこと - ログミーTech](https://logmi.jp/tech/articles/320153)
- [画像処理 in Julia 1.0 #2 - Qiita](https://qiita.com/yoyoyoh-yohyoh/items/9f13d5450066a8a85991)

## 試すこと

- スキャン方法
- 演算方法 (int, float, half, fixed-point, ...)
