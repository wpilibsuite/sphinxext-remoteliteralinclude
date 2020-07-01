import pytest

@pytest.mark.sphinx("html", testroot="simple")
def test_simple(app):
    app.builder.build_all()

    content = (app.outdir / 'index.html').read_text()

    html = ('<span class="n">Example</span> <span class="n">Domain</span>')

    assert html in content
