FROM python:3.7-slim

RUN mkdir /app

WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . .

EXPOSE 8080

ENV PYTHONUNBUFFERED 1

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --log-file=- xpypi.main:app
