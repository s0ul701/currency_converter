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

CMD ["python3", "-m", "ptvsd", "--host", "0.0.0.0", "--port", "5678", "--wait", \
    "manage.py", "runserver", "--noreload", "--nothreading", "0.0.0.0:8000"]