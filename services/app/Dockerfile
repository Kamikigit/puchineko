FROM python:3.7.0
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -qq
RUN apt-get install -y git gcc make curl sudo xz-utils file \
            swig mecab libmecab-dev mecab-ipadic \
            libopenblas-dev liblapack-dev

RUN git clone https://github.com/neologd/mecab-ipadic-neologd.git /tmp/neologd
RUN cd /tmp/neologd && ./bin/install-mecab-ipadic-neologd -n -y


RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/