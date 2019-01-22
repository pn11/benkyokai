# Introduction to Haskell

## 教科書

向井淳『入門Haskell』

## 環境構築

- GHC を使う。
- [Downloads for Linux](https://www.haskell.org/downloads/linux) にあるとおり実行。
  - ただし `apt install` の行は Ubuntu 18.04 で動かなかったのでバージョン名を外した。
  - また `$PATH` は特に通さなくても良かった。

```bash
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:hvr/ghc
sudo apt-get update
# sudo apt-get install -y cabal-install-1.22 ghc-7.10.3 # Ubuntu 18.04 で動かない
sudo apt-get install -y cabal-install ghc

#cat >> ~/.bashrc <<EOF
#export PATH="\$HOME/.cabal/bin:/opt/cabal/1.22/bin:/opt/ghc/7.10.3/bin:\$PATH"
#EOF
#export PATH=~/.cabal/bin:/opt/cabal/1.22/bin:/opt/ghc/7.10.3/bin:$PATH
```

### インストール先

```bash
$ which cabal
# /usr/bin/cabal
$ which ghc
# /usr/bin/ghc
$ which ghci
# /usr/bin/ghci
```



## Reference
