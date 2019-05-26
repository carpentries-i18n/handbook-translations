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

2. Generate the `po` files for a set of languages:
```bash
sphinx-intl update -p locale/gettext -l es -l fr
```
This generates the basic translation files for `es` and `fr` under `locale/<lang>`. These configuration is taken from the local `conf.py` file.

3. Translate! For that there are two ways. Listed below.

4. Build your translations
```bash
sphinx-build -D language=es -b html . _build/html
```

# Translations

# Update translations

1. Update the pot files from the original source.
```bash
sphinx-build -M gettext . locale -a
```

2. Update the po files for each of the languages you want:
```bash
sphinx-intl update -p locale/gettext -l es
```
This will mark the translations blocks that have changed into `fuzzy` translations.


# Read the docs

Each language needs to have its own project, and linked from the master project as translations.

