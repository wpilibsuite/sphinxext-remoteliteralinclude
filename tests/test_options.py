import pytest


@pytest.mark.sphinx("html", testroot="simple-short")
def test_simple(app):
    app.builder.build_all()

    content = (app.outdir / "index.html").read_text()

    html = '<span class="n">Example</span> <span class="n">Domain</span>'

    assert html in content


@pytest.mark.sphinx("html", testroot="simple-full")
def test_simple(app):
    app.builder.build_all()

    content = (app.outdir / "index.html").read_text()

    html = '<span class="n">Example</span> <span class="n">Domain</span>'

    assert html in content
