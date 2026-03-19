FROM postgres:16-alpine

ENV POSTGRES_INITDB_ARGS="--encoding=UTF8 --locale=C"

COPY init/01-bootstrap.sql /docker-entrypoint-initdb.d/01-bootstrap.sql

USER postgres

EXPOSE 5432
