# Commands

Command | Description | Required state
-|-|-
`ci` | Lints and runs tests.
`create-schema` | Creates the schema named by `DOCKER_DJANGO_SCHEMA`.
`db` | Forwarding alias for `psql` in the database docker container.
`install` | Installs the project from a newly cloned state, or partially installed state.
`load-completions` | Loads all project-specific shell completion.  Must be `source`d in the current shell. | `regenerate-completions` should be run first.
`logs` | Attaches to the `django`, `celery`, and `beat` services to view their logs.
`manage` | Unwrapped version of Django's `manage.py` script. | `django` service running
`manual` | Forwarding alias for `hugo` in the manual docker container (which is in itself a convenience wrapper around [`hugo`](https://gohugo.io/)).
`model-create` | Given a model name, creates and installs an app for that model.  Takes an optional second argument for the app name - defaults to the model name converted to lower_snake_case and pluralised according to some English grammar rules.
`regenerate-completions` | (Re)generates shell completion for `manage`'s subcommands. | `django` service running
`start` | Starts all of the installed project's services.
`stop` | Stops all the installed project's services.
`uninstall` | Brings the installed project back to an initial-like state, while preserving configuration.
`unload-completions` | Unloads any project-specific shell completions.  Must be `source`d in the current shell.
`update-cert` | (Re)generates local development SSL certificate.

# Other files

Path | Description
-|-
[`completions/`](completions/) | Holds generated completions for commands in this directory.
