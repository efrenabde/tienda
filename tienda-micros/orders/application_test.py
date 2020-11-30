# application_test.py
import pytest
import application
import json

@pytest.fixture
def client():
    app = application.create_app(db_uri="sqlite:///red_test.db")
    yield app.test_client()

def test_creation_order():
    app = application.create_app(db_uri="sqlite:///red_test.db")
    clientB = app.test_client()
    rs = clientB.post('/api/orders', json={
        'productos':[{
            'nombreProducto': 'Abc',
            'cantProducto':  1,
            'valorUnitario': 15413
        }],
        'descuento': 15000,
        'valorTotal': 150000,
        'idUsuario': 1
    }, follow_redirects=True)
    
    print('Respuesta', rs.status_code )
    assert rs.status_code == 201
