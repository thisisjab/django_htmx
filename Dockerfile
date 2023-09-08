from python:3.11.4-slim as base

WORKDIR /app

RUN pip install poetry==1.6.1

COPY pyproject.toml poetry.lock /app

# Read args from .env file
ARG IS_DEBUG
# ENV PROJECT_DEBUG=$PROJECT_DEBUG

# RUN if [ "$PROJECT_DEBUG" = "true" ]; then \
#         poetry export --with dev -f requirements.txt --output requirements.txt; \
#     else \
#         poetry export -f requirements.txt --output requirements.txt; \
#     fi

RUN if [ "$IS_DEBUG" = "true" ] ; then \
        poetry export --with dev -f requirements.txt --output requirements.txt; \
    else \
        poetry export -f requirements.txt --output requirements.txt; \
    fi

RUN pip install -r requirements.txt

FROM python:3.11.4-slim

COPY --from=base /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

COPY --from=base /usr/local/bin/ /usr/local/bin/

COPY . /app

WORKDIR /app

ENV PYTHONUNBUFFERED 1
