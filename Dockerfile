FROM python:3.7-alpine
# MAINTAINER Dual Junior

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN \
 apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

RUN mkdir /application
WORKDIR /application
COPY ./application /application

# Security Propourses
RUN adduser -D user
USER user


