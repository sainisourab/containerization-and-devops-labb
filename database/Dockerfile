FROM postgres:15-alpine

# Set default env variables (can be overridden by compose)
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=project1

# Copy initialization script to docker-entrypoint-initdb.d
# This script will automatically run on the first startup if the volume is empty
COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
