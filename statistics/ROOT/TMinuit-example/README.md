# TMinuit でガウシアンをフィッティングするサンプル

- ROOT のインタプリターと GNUMake 両方で使える。
- 無駄にスマートポインタ使ってみた（ROOTの例ではあまり見たことがない。）
  - ただしグローバルスコープのものは従来のポインタ。
- `TH1::Fit` と `TMinuit` でやって比較。
  - `TMinuit` は自由度が大きい分設定が大変。
  - `TH1::Fit` は簡単なのにちゃんとフィットできてすごいと再認識。
  - `TH1::Fit` でも任意の関数扱えるので、`TMinuit` をわざわざ使うべき状況は多くない。
    - 例えば複数のヒストグラムを同時にフィットしたいときなど
