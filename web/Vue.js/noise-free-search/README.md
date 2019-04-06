# 機械翻訳のクソサイトとかを除いて検索するためのやつ

## Usage

### Yarn 導入

#### Ubuntu
<https://yarnpkg.com/lang/en/docs/install/#debian-stable>


```
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
```

```
sudo apt-get update && sudo apt-get install yarn
```

#### Mac

```
brew install yarn
```

### Create Project 

```
mkdir noise-free-search
yarn init
yarn add webpack webpack-dev-server vue vue-loader vue-template-compiler
```

### Start Server

```
node_modules/.bin/webpack #webpack でコンパイル
yarn start # http://localhost:4000 にアクセスで見られる。
```

## Reference

### yarn, Webpack

- [yarnを使ってVue.jsをwebpackで導入 - TIS ENGINEER NOTE](https://tisnote.com/vue-webpack-yarn/)
- [ゼロからVue向けのウェブパック設定 - Qiita](https://qiita.com/webpack_master/items/80bb0e4d226e1882b377)

### Vue.js

- [リストレンダリング — Vue.js](https://jp.vuejs.org/v2/guide/list.html)
- [コンポーネントの基本 — Vue.js](https://jp.vuejs.org/v2/guide/components.html)
    - これを真似していったらコンポーネントが理解できた。 Vue.js は公式サイトを写経していくのが一番良い勉強方法かも。

### クソサイトについて

- [Stack Overflowの英語から日本語に機械翻訳されたコンテンツのサイトについてどう思いますか？ - スタック・オーバーフローMeta](https://ja.meta.stackoverflow.com/questions/2905/stack-overflow%E3%81%AE%E8%8B%B1%E8%AA%9E%E3%81%8B%E3%82%89%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%81%AB%E6%A9%9F%E6%A2%B0%E7%BF%BB%E8%A8%B3%E3%81%95%E3%82%8C%E3%81%9F%E3%82%B3%E3%83%B3%E3%83%86%E3%83%B3%E3%83%84%E3%81%AE%E3%82%B5%E3%82%A4%E3%83%88%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E3%81%A9%E3%81%86%E6%80%9D%E3%81%84%E3%81%BE%E3%81%99%E3%81%8B)

- [Сообщения со ссылками на спам–сайты будут блокироваться движком - Stack Overflow на русском Meta](https://ru.meta.stackoverflow.com/questions/7104/%d0%a1%d0%be%d0%be%d0%b1%d1%89%d0%b5%d0%bd%d0%b8%d1%8f-%d1%81%d0%be-%d1%81%d1%81%d1%8b%d0%bb%d0%ba%d0%b0%d0%bc%d0%b8-%d0%bd%d0%b0-%d1%81%d0%bf%d0%b0%d0%bc-%d1%81%d0%b0%d0%b9%d1%82%d1%8b-%d0%b1%d1%83%d0%b4%d1%83%d1%82-%d0%b1%d0%bb%d0%be%d0%ba%d0%b8%d1%80%d0%be%d0%b2%d0%b0%d1%82%d1%8c%d1%81%d1%8f-%d0%b4%d0%b2%d0%b8%d0%b6%d0%ba%d0%be%d0%bc)


