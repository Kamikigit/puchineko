twitterクライアントもどきです。  
Flask --- uwsgi --- nginx --- client  

# ファイル構成  
.  
├── Makefile  
├── README.md  
├── app  
│   ├── Dockerfile  
│   ├── myapp.ini  
│   ├── nginx_signing.key  
│   ├── requirements.txt  
│   ├── src  
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
