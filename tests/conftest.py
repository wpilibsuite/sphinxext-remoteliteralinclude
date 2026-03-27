import pytest
from pathlib import Path

pytest_plugins = "sphinx.testing.fixtures"


@pytest.fixture(scope="session")
def rootdir():
    return Path(__file__).parent.absolute() / "roots"


@pytest.fixture()
def content(app):
    app.build()
    yield app


def pytest_configure(config):
    config.addinivalue_line("markers", "sphinx")
