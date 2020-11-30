# application_test.py
import pytest
import application
import json

@pytest.fixture
def client():
    app = application.create_app(db_uri="sqlite:///red_test.db")
    yield app.test_client()

def test_creation_user():
    app = application.create_app(db_uri="sqlite:///red_test.db")
    clientB = app.test_client()
    rs = clientB.post('/api/users', json={
        'tipo': 1,
        'nombre': 'Clarencia'
    }, follow_redirects=True)
    
    print('Respuesta', rs.status_code )
    assert rs.status_code == 201
