# BASEDIR is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized sphinx document.
For example::
    sphinx-build -D language=ja -b html . _build/html
This conf.py do:
- Specify `locale_dirs` and `gettext_compact`.
- Overrides source directory as 'handbook/`.
"""
import os
from pathlib import Path

from sphinx.util.pycompat import execfile_


BASEDIR = Path(os.path.abspath(__file__)).parent.absolute()

execfile_(str(BASEDIR / 'handbook' / 'conf.py'), globals())

locale_dirs = [str(BASEDIR / 'locale/')]
gettext_compact = False

def setup(app):
    app.srcdir = str(BASEDIR / 'handbook/')
    app.confdir = app.srcdir
