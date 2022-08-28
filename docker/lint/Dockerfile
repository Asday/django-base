FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

RUN adduser --disabled-password --gecos '' python

RUN pip install -U pip

RUN mkdir /requirements
WORKDIR /requirements
COPY lint.txt /requirements/
RUN --mount=type=cache,target=/root/.cache pip install -r lint.txt

RUN mkdir /src
WORKDIR /src

USER python
