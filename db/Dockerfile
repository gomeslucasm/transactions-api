FROM mongo:latest

WORKDIR /data

COPY transactions.agz /data

CMD ["sh", "-c", "gunzip -c /data/dump.agz | mongorestore --archive && mongod"]