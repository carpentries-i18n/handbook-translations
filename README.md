# Quick start

First time? Update `conf.py` from the handbook (or master repository) with the following:
```python
# -- Options for translations --------------------------------------------
locale_dirs = ['../locale/']   # Defines the path for the translations.
gettext_compact = False        # Not all the files into one.

from sphinx import addnodes    # noqa # Adds a setup option that we can use in the local conf.py
```

1. In the root directory: Create the pot files with:
```bash
sphinx-build -M gettext . locale -a
```
That creates a `gettext` folder under `locale` filled with the `pot` files.

