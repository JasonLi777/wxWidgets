
"""Renamer stub: provides a way to drop the wx prefix from wxPython objects."""

from wx import _rename
from wxPython.lib import fancytext
_rename(globals(), fancytext.__dict__, modulename='lib.fancytext')
del fancytext
del _rename
