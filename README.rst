Xerox: Copy + Paste for Python
==============================

Upstream slow to to respond to PRs. Also consider https://github.com/asweigart/pyperclip where there is a PR for Wayland support.

*Xerox* is a copy + paste module for python. It's aim is simple: to be as incredibly simple as possible.

Supported platforms are currently OS X, X11 (Linux, BSD, etc.), and Windows.

If you can make it simpler, please fork.

Usage
-----

Usage is as follows::

	xerox.copy(u'some string')

And to paste::

	>>> xerox.paste()
	u'some string'

On Linux you can optionally also copy into the X selection clipboard for
middle-click-paste capability::

    xerox.copy(u'Some string', xsel=True)

And you can choose to paste from the X selection rather than the system
clipboard::

    xerox.paste(xsel=True)

On Windows you can optionally copy into the clipboard in html mode::

    xerox.copy(u'<p>Writing to the clipboard is <strong>easy</strong> with this code.</p>', html=True)

This will also paste the html into the text clipboard for applications
that do not support html mode.
HTML paste from the clipboard is not implemented. Unlike xsel support,
there is no silent failure if html mode is requested with a backend
that does not support it.

And, that's it.

Command Line
~~~~~~~~~~~~

To copy::

	$ xerox some string

or::

	$ echo some string | xerox

To paste::

	>>> xerox
	some string


Installation
------------

To install Xerox, simply::

	$ pip install xerox

Note: If you are installing xerox on Windows, you will also need to install the pywin32_ module.

Note: On X11 systems, Xerox requires Xclip, which can be found through your system package manager (e.g. apt-get install xclip) or at https://github.com/astrand/xclip


To Do Items
-----------

* Android support
* RTF copy support (for Windows and xclip)

Legal Stuff
-----------

MIT License.

(c\) 2016 Kenneth Reitz.

.. _pywin32: http://sourceforge.net/projects/pywin32/files/
