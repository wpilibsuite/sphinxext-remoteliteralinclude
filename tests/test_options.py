import os
import pytest
from sphinx.application import Sphinx
from sphinx import version_info
from sphinx.config import Config
from sphinxext.remoteliteralinclude import RemoteLiteralIncludeReader


DUMMY_CONFIG = Config({}, {})


@pytest.mark.sphinx("html", testroot="simple-short")
def test_simple_short(app: Sphinx):
    app.build()

    content = read_text(app)

    html = '<span class="n">Example</span> <span class="n">Domain</span>'

    assert html in content


@pytest.mark.sphinx("html", testroot="simple-full")
def test_simple_full(app: Sphinx):
    app.build()

    content = read_text(app)

    html = '<span class="n">Example</span> <span class="n">Domain</span>'

    assert html in content


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
