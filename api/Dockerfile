FROM python:3.11-slim

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root

COPY . /app

EXPOSE 8888

CMD ["poetry", "run", "python", "main.py"]