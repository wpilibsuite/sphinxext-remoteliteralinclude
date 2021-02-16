import pytest
from sphinx.application import Sphinx
from sphinx import version_info


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


def read_text(app: Sphinx):
    if version_info[:2] < (3, 0):
        return (app.outdir / "index.html").text().replace("\n", "")
    else:
        return (app.outdir / "index.html").read_text()
