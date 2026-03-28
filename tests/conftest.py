import pytest

# try to import the old testing path helper; keep it available for older Sphinx
try:
    from sphinx.testing.path import path  # type: ignore
except Exception:
    path = None

from pathlib import Path

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(scope="session")
def rootdir():
    # use sphinx.testing.path if availible (removed in Sphinx 9, else use pathlib, which fails with older Sphinx versions)
    if path is not None:
        return path(__file__).parent.abspath() / "roots"
    if Path is not None:
        return Path(__file__).parent.resolve() / "roots"
    # last resort
    return Path(__file__).parent.resolve() / "roots"


@pytest.fixture()
def content(app):
    app.build()
    yield app


def pytest_configure(config):
    config.addinivalue_line("markers", "sphinx")
