""" Copy + Paste in Windows
"""

# found @ http://code.activestate.com/recipes/150115/

from .base import * 

try:
    import win32clipboard
    import win32clipboard as clip
    import win32con
except ImportError as why:
    raise Pywin32NotFound

CF_HTML = win32clipboard.RegisterClipboardFormat("HTML Format")


def copy(string, html=False, **kwargs):
    """Copy given string into system clipboard."""

    if html:
        # Extracted from https://gist.github.com/Erreinion/6691093/b2e91a7abf92ac08dce6da9060c99c627c993472
        DEFAULT_HTML_BODY = \
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 Transitional//EN\">" \
            "<HTML><HEAD></HEAD><BODY><!--StartFragment-->%s<!--EndFragment--></BODY></HTML>"

        MARKER_BLOCK_OUTPUT = \
            "Version:1.0\r\n" \
            "StartHTML:%09d\r\n" \
            "EndHTML:%09d\r\n" \
            "StartFragment:%09d\r\n" \
            "EndFragment:%09d\r\n" \
            "StartSelection:%09d\r\n" \
            "EndSelection:%09d\r\n" \
            "SourceURL:%s\r\n"

        def EncodeClipboardSource(html, fragmentStart, fragmentEnd, selectionStart, selectionEnd, source):
            """
            Join all our bits of information into a string formatted as per the HTML format specs.
            """
            # How long is the prefix going to be?
            dummyPrefix = MARKER_BLOCK_OUTPUT % (0, 0, 0, 0, 0, 0, source)
            lenPrefix = len(dummyPrefix)

            prefix = MARKER_BLOCK_OUTPUT % (lenPrefix, len(html)+lenPrefix,
                            fragmentStart+lenPrefix, fragmentEnd+lenPrefix,
                            selectionStart+lenPrefix, selectionEnd+lenPrefix,
                            source)
            return (prefix + html)

        selection = None
        html_str = None
        source = None
        """
        Put the given well-formed fragment of Html into the clipboard.

        selection, if given, must be a literal string within fragment.
        html_str, if given, must be a well-formed Html document that textually
        contains fragment and its required markers.
        """
        if selection is None:
            selection = string
        if html_str is None:
            html_str = DEFAULT_HTML_BODY % string
        if source is None:
            source = "file://xerox.py"

        fragmentStart = html_str.index(string)
        fragmentEnd = fragmentStart + len(string)
        selectionStart = html_str.index(selection)
        selectionEnd = selectionStart + len(selection)
        try:
            win32clipboard.OpenClipboard(0)
            win32clipboard.EmptyClipboard()
            src = EncodeClipboardSource(html_str, fragmentStart, fragmentEnd, selectionStart, selectionEnd, source)
            src = src.encode("UTF-8")
            win32clipboard.SetClipboardData(CF_HTML, src)
            print(repr(src))
            win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, string)  # set plain text as well as the html above
        finally:
            win32clipboard.CloseClipboard()
    else:
        clip.OpenClipboard()
        clip.EmptyClipboard()
        clip.SetClipboardData(win32con.CF_UNICODETEXT, string) 
        clip.CloseClipboard()

    return

def paste(**kwargs):
    """Returns system clipboard contents."""

    clip.OpenClipboard() 
    try:
        d = clip.GetClipboardData(win32con.CF_UNICODETEXT)
    except TypeError:
        # Handle, "Specified clipboard format is not available"
        # Either clipboard is empty or does NOT contain text
        d = ''
    clip.CloseClipboard() 
    return d 

 
