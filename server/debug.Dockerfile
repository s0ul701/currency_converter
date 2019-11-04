FROM python:3.8.0-buster

RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends && \
  apt-get autoremove -y && \
  mkdir /server

WORKDIR /server

COPY ./server/ /server

RUN pip install -r requirements.txt

RUN pip install ptvsd