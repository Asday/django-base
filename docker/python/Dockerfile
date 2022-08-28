FROM python:3.10-alpine as stage0

ENV PYTHONUNBUFFERED 1

RUN --mount=type=cache,target=/var/cache/apk \
  apk add --virtual .build-deps \
  gcc \
  make \
  python3-dev \
  musl-dev \
  postgresql-dev \
  && pip install -U pip \
  && apk add --no-cache libpq shadow

FROM stage0 as build
ARG requirements

RUN mkdir /requirements
WORKDIR /requirements
COPY requirements/${requirements} /requirements/

RUN --mount=type=cache,target=/root/.cache \
  printf -- '-r\0%s\0' *.txt | xargs -0 pip install

RUN apk del --no-cache .build-deps


FROM python:3.10-alpine
ARG docker_uid
ARG docker_gid

ENV PYTHONUNBUFFERED 1

COPY --from=build etc /etc
COPY --from=build lib /lib
COPY --from=build usr /usr

RUN adduser \
    --disabled-password \
    --gecos '' \
    -u ${docker_uid} \
    python \
  && groupmod -g ${docker_gid} python \
  && mkdir /src \
  && mkdir -p /srv/media /srv/static \
  && chown -R python:python /srv /home/python
WORKDIR /src

USER python
