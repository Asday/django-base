# Files

Path | Description
-|-
[`requirements/`](requirements/) | Repository for sets of hardlinked Python requirements files to build specific docker containers.
[`storage/`](storage/) | Persistent storage for Django static and uploaded files.  Static files are gitignored as their source of truth is the app directories, and media files are gitignored as they're a development artefact.
`Dockerfile` | Build file for all Python docker containers.
