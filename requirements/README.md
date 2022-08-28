# Requirements

This directory is the source of truth for Python requirements files.  The files here are hardlinked to the appropriate locations by [`install`](../bin/install), then acted upon based on build arguments passed to [the base Python `Dockerfile`](../docker/python/Dockerfile).

# Files

Path | Description
-|-
`base.txt` | Requirements for the base project, i.e., everything in `src/`.  Deployment-specific requirements such as a WSGI/ASGI server and database engine which the project leaves unconstrained do not belong in this file.
`database.txt` | Requirements for the deployment inside docker, currently the database and key-value store choices named in [`docker-compose.yml`](../docker-compose.yml).
`lint.txt` | Requirements for linting the project, which are entirely standalone.
`test.txt` | Requirements for running unit tests, which shouldn't be present on production deployments.
`webserver.txt` | Requirements for running the project's web server as named in [`docker-compose.yml`](../docker-compose.yml).
