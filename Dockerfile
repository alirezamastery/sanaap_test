FROM python:3.12.6-slim-bookworm

RUN apt update && apt install -y supervisor libpq-dev

WORKDIR /src

COPY ./src/requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /src/requirements.txt

COPY ./src/ .

EXPOSE 8000

RUN mkdir -p /etc/supervisor/conf.d
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY ./docker-entrypoint.sh ./docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
