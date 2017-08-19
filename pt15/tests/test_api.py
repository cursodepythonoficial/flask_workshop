import pytest
from flask import url_for


def test_sum(client):
    response = client.post(
        url_for('api', operation='sum'), data={'x': 10, 'y': 4}
    )
    assert response.json['result'] == 14


def test_mul(client):
    response = client.post(
        url_for('api', operation='mul'), data={'x': 10, 'y': 4}
    )
    assert response.json['result'] == 40


def test_sub(client):
    response = client.post(
        url_for('api', operation='sub'), data={'x': 10, 'y': 4}
    )
    assert response.json['result'] == 6


def test_div(client):
    response = client.post(
        url_for('api', operation='div'), data={'x': 10, 'y': 4}
    )
    assert response.json['result'] == 2.5


def test_empty_data_raises_error(client):
    with pytest.raises(TypeError):
        client.post(url_for('api', operation='div'))
