from fastapi.testclient import TestClient
from dependencies import get_db
from utils.client_utils import get_client_name_util, delete_client_util
from utils.movements_utils import create_movement_util, MovementCreate
import pytest
from main import app


client = TestClient(app)

URL = "/api/movements"

CLIENT_DATA = {"name": "Test Client"}


@pytest.fixture
def create_client():
    client.post("/api/client/create", json=CLIENT_DATA)
    client_db = get_client_name_util(next(get_db()), CLIENT_DATA["name"])
    return client_db


@pytest.fixture
def clean_client():
    yield
    client_db = get_client_name_util(next(get_db()), CLIENT_DATA["name"])
    delete_client_util(next(get_db()), client_db.id)


def test_register_movement(create_client, clean_client):
    data = {"id_account": create_client.accounts[0].id, "type": "income", "amount": 200}
    response = client.post(f"{URL}/register", json=data)
    assert response.status_code == 200
    assert response.json() == data


def test_failed_account_register_movement():
    data = {"id_account": 0, "type": "income", "amount": 200}
    response = client.post(f"{URL}/register", json=data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Account not found"}


def test_failed_egress_balanced_register_movement(create_client, clean_client):
    data = {"id_account": create_client.accounts[0].id, "type": "egress", "amount": 200}
    response = client.post(f"{URL}/register", json=data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Exceeds available balance"}


def test_delete_movement_endpoint(create_client, clean_client):
    movement_data = MovementCreate(id_account=create_client.accounts[0].id, type="income", amount=200)
    movement_db = create_movement_util(next(get_db()), movement_data)
    response = client.delete(f"{URL}/{movement_db.id}/delete")
    assert response.status_code == 200
    assert response.json()["id_account"] == movement_db.id_account


def test_failed_delete_movement_endpoint():
    response = client.delete(f"{URL}/0/delete")
    assert response.status_code == 404
    assert response.json() == {"detail": "movement not found"}


def test_get_movement_endpoint(create_client, clean_client):
    movement_data = MovementCreate(id_account=create_client.accounts[0].id, type="income", amount=200)
    movement_db = create_movement_util(next(get_db()), movement_data)
    response = client.get(f"{URL}/{movement_db.id}")
    assert response.status_code == 200
    assert response.json()["id_account"] == movement_db.id_account


def test_failed_get_movement_endpoint():
    response = client.get(f"{URL}/0")
    assert response.status_code == 404
    assert response.json() == {"detail": "movement not found"}
