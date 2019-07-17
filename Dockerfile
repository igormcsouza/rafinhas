FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt

COPY ./docker-entrypoint.sh /docker-entrypoint.sh

RUN apk update && \
    apk add --no-cache python3 postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
    apk --purge del .build-deps && \
    chmod +x /docker-entrypoint.sh && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

COPY ./application /opt/application

WORKDIR /opt/application

ENTRYPOINT [ "/docker-entrypoint.sh" ]