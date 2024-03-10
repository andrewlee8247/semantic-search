import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.main import app


@pytest.fixture(scope="module")
def test_app():
    with TestClient(app) as client:
        yield client
