# Files

Path | Directory
-|-
[`celery/`](celery/) | Python requirements files for the asynchronous task runner part of the project.
[`django/`](default/) | Python requirements files for the web application part of the project.
[`test/`](test/) | Python requirements files that describe the base project's dependencies, plus all dependencies required to run the test suite.

Note that the source of truth for requirements files is in [`PROJECT_ROOT/requirements/`](../../../requirements/), but files under this directory are hardlinked, so editing either will work.  Just be aware that if files in multiple subdirectories here share the same name but need to diverge, new files and hardlinks will need to be made, as well as updating [`install`](../../../bin/install).
