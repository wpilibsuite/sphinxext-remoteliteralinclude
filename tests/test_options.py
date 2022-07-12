import os
import pytest
from sphinx.application import Sphinx
from sphinx import version_info
from sphinx.config import Config
from sphinxext.remoteliteralinclude import RemoteLiteralIncludeReader


DUMMY_CONFIG = Config({}, {})


def test_simple_short():
    # Use a known stable example website
    url = "http://example.com/"
    options = {"lines": "4-4"}
    # grab the html on lines 4
    reader = RemoteLiteralIncludeReader(url, options, DUMMY_CONFIG)
    content, lines = reader.read()

    actual_content = f"    <title>Example Domain</title>{os.linesep}"

    # Check lines 4, and that it only returned 1 line
    assert content == actual_content
    assert lines == 1


def test_simple_full():
    # Use a known stable example website
    url = "http://example.com/"
    options = {}
    # grab the html
    reader = RemoteLiteralIncludeReader(url, options, DUMMY_CONFIG)
    content, lines = reader.read()

    sub_content = f"    <title>Example Domain</title>{os.linesep}"

    # Check a subcontent to make it more robust to their website changing
    assert sub_content in content
    assert lines == 46


def test_pyobject():
    url = "https://raw.githubusercontent.com/wpilibsuite/sphinxext-remoteliteralinclude/main/sphinxext/remoteliteralinclude.py"
    # Grab the entire RemoteLiteralIncludeReader.__init__
    options = {"pyobject": "RemoteLiteralIncludeReader.__init__"}
    reader = RemoteLiteralIncludeReader(url, options, DUMMY_CONFIG)
    content, lines = reader.read()

    # only check the first line to be less susceptible to breaking with code changes
    first_line = "    def __init__(self, url, options, config):"
    assert content.splitlines()[0] == first_line

    # we grab just the second line from `RemoteLiteralIncludeReader`
    options = {"pyobject": "RemoteLiteralIncludeReader", "lines": "2-2"}
    reader = RemoteLiteralIncludeReader(url, options, DUMMY_CONFIG)
    content, lines = reader.read()

    # we use os.linesep to replace with \n on posix and \r\n on windows
    second_line = f"    INVALID_OPTIONS_PAIR = [{os.linesep}"  # this keeps \n because no splitlines
    assert content == second_line


def read_text(app: Sphinx):
    if version_info[:2] < (3, 0):
        return (app.outdir / "index.html").text().replace("\n", "")
    else:
        return (app.outdir / "index.html").read_text()
