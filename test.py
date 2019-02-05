import json

import pytest

from app import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def testClientExists(client):
    response = client.get('/')
    assert b'Robot ready!' in response.data
