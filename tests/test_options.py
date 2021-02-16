import pytest
from sphinx.application import Sphinx


@pytest.mark.sphinx("html", testroot="simple-short")
def test_simple_short(app: Sphinx):
    app.build()

    content = (app.outdir / "index.html").read_text()

    html = '<span class="n">Example</span> <span class="n">Domain</span>'

    assert html in content


@pytest.mark.sphinx("html", testroot="simple-full")
def test_simple_full(app: Sphinx):
    app.build()

    content = (app.outdir / "index.html").read_text()

    html = '<span class="n">Example</span> <span class="n">Domain</span>'

    assert html in content
