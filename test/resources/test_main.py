"""Tests of main resources."""
import pytest


def test_environment(factory_app):
    """Test of the application environment."""
    assert factory_app.environment == 'testing'


@pytest.mark.parametrize('http_method,http_path', (
    ('GET', '/api/hello/test'),
))
def test_helloworld(http_method, http_path, flask_app_client):
    """Test of HelloWorld class."""
    response = flask_app_client.open(method=http_method, path=http_path)
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json == {'hello': 'test'}
