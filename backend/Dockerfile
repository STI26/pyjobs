FROM python:latest
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
RUN mkdir -p /media
COPY requirements/base.txt /usr/src/app/
COPY requirements/production.txt /usr/src/app/
RUN pip install -r base.txt
RUN pip install -r production.txt
COPY . /usr/src/app/