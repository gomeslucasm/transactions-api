# Tornado API Project

Este projeto implementa uma API usando o framework Tornado para interagir com um banco de dados MongoDB. A API possui endpoints para verificar o status da aplicação, obter o TPV (Total Payment Volume) e listar transações por data com paginação.

## Como rodar o projeto

### 1. Rodar o Docker Compose

Para iniciar os serviços definidos no Docker Compose, execute:

```sh
docker-compose up --build
```

### 2. Adicionar o dump do banco de dados

Siga os passos abaixo para adicionar o dump do banco de dados:

    Copie o arquivo de dump para o contêiner do MongoDB:

```bash
docker cp transactions.agz db:/transactions.agz
docker exec -it db mongorestore --uri 'mongodb://admin:admin@db:27017' --archive=/transactions.agz --gzip
```
