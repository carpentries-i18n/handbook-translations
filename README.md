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

## Locally

There are plenty of tools that allows the visualisation of the po files. You can use these and create a PR to this project.

## Collaboratively

We, for now, will use transifex as tool for collaborative translations.

### Setup (only the first time)

Assuming the project has already been created on the web.
We need to install the transifex client (`pip install ttransifex-client`) and initialise it with:

```bash
tx init
```
That will ask you a set of questions about the project and your tx account. Follow them as if you would use only a single file:
```
[?] Enter the path to your local source file: locale/gettext/index.pot
[?] Enter a path expression: locale/<lang>/LC_MESSAGES/index.po
[?] Select the file format type [1]: 1
[?] Select the organization to use [1-3]: 1
[?] Select the project to use [1-6]: 4
```

Then run this line to generate the mapping to all the files
```bash
tx config mapping-bulk -p handbook-translations --source-language en --type PO -f '.pot' --source-file-dir locale/pot --expression "locale/<lang>/LC_MESSAGES/{filepath}/{filename}.po" --execute
```
and delete the entry created with the interactive script from the `.tx/config` file.

I've got this command - but I don't know yet what it does:
```bash
tx config mapping-remote  https://www.transifex.com/carpentries-es/handbook-translations
```

All right, let's push the sources to the website:
```bash
tx push -s
```

and to push translations:
```bash
tx push -t -l es
```

# Update translations

## Download translations from transifex

To download all the translations, first we change to the `<lang>` branch (we are keeping them separated because Read The Docs is pulling from branches)

```bash
tx pull -l <lang>
```
(If that fails to download the translations, then use the `-f` flag to force the downloading)

To download only reviewed translations then you can use:

```bash
tx pull -a -l es --mode reviewed
```

## Build the documentation locally

Still on the same branch, run:

```bash
make -e SPHINXOPTS="-D language='es'" html
cd _build/html
python -m http.server
```

and open the given url (e.g., http://0.0.0.0:8000) in your browser.

## Build the documentation on Read The Docs

For the moment, these "un-official" docs are being built on [Read the Docs](https://carpentrieshandbook.readthedocs.io/).
They are built by pulling from the `<lang>` branch. Only the Spanish translations (`es`) have been set-up at the moment.
To update the translations after pulling them from transifex as explained above, we need to push that branch to github.

```bash
git add locale/<lang>/*
git commit -m "Translations done in Sanish up to <month> <day>"
git push origin <lang>
```

After a few seconds the latest update should be available on the website. The status of the builds can be found at [the Read the Docs' dashboard](https://readthedocs.org/projects/carpentrieshandbook-es/builds/)

## Update translation files when sources has changed (TODO)

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

+
