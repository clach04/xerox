import sys

from .base import Pywin32NotFound

if sys.platform == 'darwin':
    from .darwin import *

elif sys.platform == 'win32':
    try:
        from .win import *
    except ImportError:
        from .tkinter import *
    except Pywin32NotFound:  # optional, this allows fallback to tk
        from .tkinter import *

elif sys.platform == 'cli':
    from .cli import *

else:
    from .x11 import *
