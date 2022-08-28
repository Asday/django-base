# `src/`

This directory contains only the source code for the project, with no particular opinion on how to run it, test it, or deploy it.

# Files

Path | Description
-|-
[`_/`](_/) | Django project settings.
[`wait_for_db/`](wait_for_db/) | Self-contained app providing a management command that blocks until the database is awake and ready, or times out and returns a non-zero exit code.
