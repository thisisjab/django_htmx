from python:3.11.4-slim as base

WORKDIR /app

RUN pip install poetry==1.6.1

COPY pyproject.toml poetry.lock /app

RUN poetry export -f requirements.txt --output requirements.txt

RUN pip install -r requirements.txt

FROM python:3.11.4-slim

COPY --from=base /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

COPY --from=base /usr/local/bin/ /usr/local/bin/

COPY . /app

WORKDIR /app

ENV PYTHONUNBUFFERED 1
