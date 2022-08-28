# Manual

Documentation for end users.  If a feature isn't documented here, it doesn't exist.  If a feature's behaviour differs from how it's documented here, it's a bug.

# Developing

[`docker-compose.yml:manual`](../docker-compose.yml) runs `hugo` as a server in watch mode with autorebuilding and autoreloading.  This is accessible at `127.0.0.1` on the port defined by `$DOCKER_HUGO_PORT`, by default `1313`.

To add a new page to the manual, run `manual new docs/<page_title>.md`.  Sections in the manual are determined by file structure, with the caveat that only directories with an `_index.md` are considered sections.  `manual new docs/<section_title>/_index.md` will generate what's required.

# Exporting

Run `manual build` (prefaced by an optional `rm -r public/`) to export the site as static HTML and assets to [`public/`](public/).  This can then be deployed on anything with an HTTP server via `rsync` or FTP, or basically anything else capable of transferring files.

# Files

Path | Description
-|-
`archetypes/` <br /> `data/` <br /> `layouts/` <br /> `resources/` <br /> `static/` | Assets and data used to build the static site.  See [the docs](https://gohugo.io/getting-started/directory-structure/) for in-depth information.
[`content/`](content/) | Plaintext content files used to build the static site, one per page.  Generate new pages with `manual new <path>`.
`.hugo-build.lock` | Semaphore used by the Hugo server when running.
`config.toml` | Configuration for the generated static site.  See the [Hugo](https://gohugo.io/getting-started/configuration/) and [theme](https://github.com/alex-shpak/hugo-book/blob/v9/README.md#configuration) docs for possible keys and values.
