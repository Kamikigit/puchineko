FROM python:3.6
RUN mkdir /var/www
WORKDIR /var/www
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /var/www/src
# コンテナが起動したときに実行される命令を指定
CMD ["uwsgi","--ini","/var/www/myapp.ini"]

