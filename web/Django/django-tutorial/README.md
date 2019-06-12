# Django Tutorial

- [さぁ始めましょう | Django ドキュメント | Django](https://docs.djangoproject.com/ja/2.2/intro/)
- [WebFrameworks - Python Wiki](https://wiki.python.org/moin/WebFrameworks)
  - Python Webフレームワークの比較。

```bash
$ python -m django --version
2.2.2
```

サーバーを起動

```sh
$ django-admin startproject mysite
$ cd mysite
$ python manage.py runserver
...
```

これで <http://127.0.0.1:8000/> に立つ。

![django_start.png](figs/django_start.png)

サーバーの IP, port を指定するには

```sh
$ python manage.py runserver 0:8000
...
```

のようにする。

## polls application

```sh
python manage.py startapp polls
```

以下を編集。

- [mysite/polls/urls.py](mysite/polls/urls.py)
- [mysite/mysite/urls.py](mysite/mysite/urls.py)

```sh
python manage.py runserver
```

して <http://127.0.0.1:8000/polls> にアクセス。
