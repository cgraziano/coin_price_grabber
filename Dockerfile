FROM python:3.7-alpine

RUN pip install requests 

ADD . /app
WORKDIR /app

ENTRYPOINT ["python", "app.py"]

