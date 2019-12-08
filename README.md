twitterクライアントもどきです。
Flask --- uwsgi --- nginx --- client

# ファイル構成
.
├── Makefile
├── README.md
├── app
│   ├── Dockerfile
│   ├── __pycache__
│   │   ├── app.cpython-36.pyc
│   │   ├── keys.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── gi --pl\033:q
│   ├── myapp.ini
│   ├── nginx_signing.key
│   ├── requirements.txt
│   ├── src
│   │   ├── __pycache__
│   │   │   └── keys.cpython-36.pyc
│   │   ├── app.py
│   │   ├── checkip.py
│   │   ├── keys.py
│   │   ├── static
│   │   │   ├── clicked.js
│   │   │   └── style.css
│   │   ├── templates
│   │   │   ├── index.html
│   │   │   ├── style.css
│   │   │   └── twitter.png
│   │   ├── testjson.py
│   │   └── wsgi.py
│   └── vol
├── docker-compose.yml
└── nginx
    ├── Dockerfile
    └── nginx.conf

8 directories, 24 files
