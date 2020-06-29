import json
import os
from pathlib import Path
from typing import List

import pytest
from bs4 import BeautifulSoup, Tag
from sphinx.application import Sphinx
from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"

@pytest.fixture(scope="session")
def rootdir():
    return path(__file__).parent.abspath() / "roots"


@pytest.fixture()
def content(app: Sphinx):
    _setup_local_user_config(app)
    app.build()
    yield app

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "sphinx"
    )
