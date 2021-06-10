FROM postgis/postgis:13-3.1

COPY load-extensions.sh /docker-entrypoint-initdb.d/