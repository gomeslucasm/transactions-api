FROM python:3.11-slim

ENV VIRTUAL_ENV=/opt/venv 
RUN python3 -m venv $VIRTUAL_ENV 
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir app && cd app

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN pip install poetry

RUN poetry export --format=requirements.txt > requirements.txt

RUN apt-get update && \
    pip install -r requirements.txt

COPY . /app

CMD ["python3", "-u", "main.py"]