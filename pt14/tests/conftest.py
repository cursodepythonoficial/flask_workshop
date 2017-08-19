import pytest
from ..app import app as myapp


@pytest.fixture
def app():
    """Flask Pytest uses it"""
    return myapp
