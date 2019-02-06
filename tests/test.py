import json
import sqlite3 as sql
import pytest
import os

from app import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_main_page(client):
    response = client.get('/')
    assert response.status_code == 200


def test_yoti_input(client):
    payload = {
        'roomSize': [5, 5],
        'coords': [1, 2],
        'patches': [
            [1, 0],
            [2, 2],
            [2, 3]
        ],
        'instructions': 'NNESEESWNWW'
    }

    payload = json.dumps(payload)

    response = client.post('/navigate',
                           data=payload,
                           content_type='application/json')

    data = json.loads(response.data)
    print(data)
    assert data['coords'] == [1, 3] and data['patches'] == 1


def test_logic_normal(client):
    payload = {
        'roomSize': [5, 5],
        'coords': [2, 2],
        'patches': [
            [0, 2],
            [2, 1],
            [3, 4]
        ],
        'instructions': 'SSWWNNNNEEE'
    }

    payload = json.dumps(payload)

    response = client.post('/navigate',
                           data=payload,
                           content_type='application/json')

    data = json.loads(response.data)
    assert data['coords'] == [3, 4] and data['patches'] == 3


def test_logic_double_patch_clean(client):
    payload = {
        'roomSize': [6, 6],
        'coords': [3, 0],
        'patches': [
            [3, 2],
            [5, 3]
        ],
        'instructions': 'NNSNEEWN'
    }

    payload = json.dumps(payload)

    response = client.post('/navigate',
                           data=payload,
                           content_type='application/json')

    data = json.loads(response.data)
    assert data['coords'] == [4, 3] and data['patches'] == 1



def test_logic_wall(client):
    payload = {
        'roomSize': [6, 6],
        'coords': [3, 1],
        'patches': [
            [4, 1],
            [5, 1]
        ],
        'instructions': 'EEEEEE'
    }

    payload = json.dumps(payload)

    response = client.post('/navigate',
                           data=payload,
                           content_type='application/json')

    data = json.loads(response.data)
    assert data['coords'] == [5, 1] and data['patches'] == 2


def test_input_validation_1(client):
    payload = {
        'roomSize': [6, 6, 4],
        'coords': [3, 1],
        'patches': [
            [4, 1],
            [5, 1]
        ],
        'instructions': 'NSSWES'
    }

    payload = json.dumps(payload)

    response = client.post('/navigate',
                           data=payload,
                           content_type='application/json')

    data = json.loads(response.data)
    assert data['error'] == 'Room size must be numeric coordinates in the form [x, y]'


def test_input_validation_2(client):
    payload = {
        'roomSize': [6, 6],
        'coords': [8, 1],
        'patches': [
            [4, 1],
            [5, 1]
        ],
        'instructions': 'NSSWES'
    }

    payload = json.dumps(payload)

    response = client.post('/navigate',
                           data=payload,
                           content_type='application/json')

    data = json.loads(response.data)
    assert data['error'] == 'Starting coordinates must be numeric coordinates in the form [x, y] and within ' \
                            'constraints of room size'


def test_input_validation_3(client):
    payload = {
        'roomSize': [6, 6],
        'coords': [2, 1],
        'patches': [
            [4, 1],
            [5, 1, 'a']
        ],
        'instructions': 'NSSWES'
    }

    payload = json.dumps(payload)

    response = client.post('/navigate',
                           data=payload,
                           content_type='application/json')

    data = json.loads(response.data)
    assert data['error'] == 'All patches must be numeric coordinates in the form [x, y] and within constraints of ' \
                            'room size'


def test_input_validation_4(client):
    payload = {
        'roomSize': [6, 6],
        'coords': [2, 1],
        'patches': [
            [4, 1],
            [5, 1]
        ],
        'instructions': 'NSS6WES'
    }

    payload = json.dumps(payload)

    response = client.post('/navigate',
                           data=payload,
                           content_type='application/json')

    data = json.loads(response.data)
    assert data['error'] == 'Instructions must be a string only containing the letters N, E, S, W'



def test_database_insert(client):
    payload = {
        'roomSize': [5, 5],
        'coords': [1, 2],
        'patches': [
            [1, 0],
            [2, 2],
            [2, 3]
        ],
        'instructions': 'NNESEESWNWW'
    }

    response = client.post('/navigate', data=payload, content_type='application/json')

    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM output")

    output = cur.fetchall()
    con.close()
