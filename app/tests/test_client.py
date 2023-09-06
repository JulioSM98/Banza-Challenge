from fastapi.testclient import TestClient

from utils.client_utils import delete_client_util, get_client_name_util, get_all_clients_util, get_avalible_balance_util, AccountBalance
import pytest
from dependencies import get_db
from main import app


from utils.movements_utils import create_movement_util, MovementCreate

client = TestClient(app)

URL = "/api/client"

CLIENT_DATA = {"name": "Test Client"}


@pytest.fixture
def create_client():
    client.post(f"{URL}/create", json=CLIENT_DATA)
    client_db = get_client_name_util(next(get_db()), CLIENT_DATA["name"])
    return client_db


@pytest.fixture
def clean_client():
    yield
    client_db = get_client_name_util(next(get_db()), CLIENT_DATA["name"])
    delete_client_util(next(get_db()), client_db.id)


def test_register_client(clean_client):
    response = client.post(f"{URL}/create", json=CLIENT_DATA)
    assert response.status_code == 200
    assert response.json() == CLIENT_DATA


def test_duplicated_register_client(create_client, clean_client):
    client.post(f"{URL}/create", json=CLIENT_DATA)
    response = client.post(f"{URL}/create", json=CLIENT_DATA)
    assert response.status_code == 400
    assert response.json() == {"detail": "Client already registered"}


def test_update_client(create_client, clean_client):
    new_client_data = {"name": "Test Client Update"}
    response = client.put(f"{URL}/update/{create_client.id}", json=new_client_data)
    client.put(f"{URL}/update/{create_client.id}", json=CLIENT_DATA)
    assert response.status_code == 200
    assert response.json() == new_client_data


def test_duplicated_update_client(create_client, clean_client):
    response = client.put(f"{URL}/update/{create_client.id}", json=CLIENT_DATA)
    assert response.status_code == 400
    assert response.json() == {"detail": "Client Name already registered"}


def test_not_found_update_client():
    client_data = {"name": "failed"}
    response = client.put(f"{URL}/update/-1", json=client_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Client not found"}


def test_delete_client(create_client):
    response = client.delete(f"{URL}/delete/{create_client.id}")
    assert response.status_code == 200
    assert response.json() == CLIENT_DATA


def test_failed_delete_client():
    response = client.delete(f"{URL}/delete/-1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Client not found"}


def test_get_all_clients(create_client, clean_client):
    all_clients = get_all_clients_util(next(get_db()))
    response = client.get(f"{URL}/get-all-clients")
    assert response.status_code == 200
    assert len(response.json()) == len(all_clients)


def test_add_client_category(create_client, clean_client):
    client_data = {"id_client": create_client.id, "id_category": 1}
    response = client.post(f"{URL}/add-client-category", json=client_data)
    assert response.status_code == 200
    assert response.json() == {"category": {"name": "Persona Fisica"}, "client": {"name": CLIENT_DATA["name"]}}


def test_failed_already_add_client_category(create_client, clean_client):
    client_data = {"id_client": create_client.id, "id_category": 1}
    client.post(f"{URL}/add-client-category", json=client_data)
    response = client.post(f"{URL}/add-client-category", json=client_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Client already in category"}


def test_failed_category_add_client_category(create_client, clean_client):
    client_data = {"id_client": create_client.id, "id_category": 0}
    response = client.post(f"{URL}/add-client-category", json=client_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Client o Category not found"}


def test_failed_client_add_client_category():
    client_data = {"id_client": 0, "id_category": 1}
    response = client.post(f"{URL}/add-client-category", json=client_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Client not found"}


def test_get_all_data_client(create_client, clean_client):
    response = client.get(f"{URL}/{create_client.id}")
    assert response.status_code == 200
    assert response.json()["name"] == create_client.name


def test_failed_get_all_data_client():
    response = client.get(f"{URL}/0")
    assert response.status_code == 404
    assert response.json() == {"detail": "Client not found"}


def test_get_categorys_client(create_client, clean_client):
    client_data = {"id_client": create_client.id, "id_category": 1}
    client.post(f"{URL}/add-client-category", json=client_data)
    response = client.get(f"{URL}/{create_client.id}/categorys")
    assert response.status_code == 200
    assert response.json() == {"categorys": [{"category": {"name": "Persona Fisica", "id": 1}}]}


def test_failed_get_categorys_client():
    response = client.get(f"{URL}/0/categorys")
    assert response.status_code == 404
    assert response.json() == {"detail": "Client not found"}


def test_get_accounts_client(create_client, clean_client):
    account = create_client.accounts
    response = client.get(f"{URL}/{create_client.id}/accounts")
    assert response.status_code == 200
    assert response.json() == {"accounts": [{"id": account[0].id}]}


def test_failed_get_accounts_client():
    response = client.get(f"{URL}/0/accounts")
    assert response.status_code == 404
    assert response.json() == {"detail": "Client not found"}


def test_get_avalible_balance(create_client, clean_client):
    movement_data = MovementCreate(id_account=create_client.accounts[0].id, type="income", amount=200)
    create_movement_util(next(get_db()), movement_data)
    avalible_db = get_avalible_balance_util(next(get_db()), create_client.id)
    response = client.get(f"{URL}/{create_client.id}/balance")
    assert response.status_code == 200
    assert [AccountBalance(**data) for data in response.json()] == avalible_db


def test_failed_client_get_avalible_balance():
    response = client.get(f"{URL}/0/balance")
    assert response.status_code == 404
    assert response.json() == {"detail": "Client not found"}


def test_failed_movement_get_avalible_balance(create_client, clean_client):
    response = client.get(f"{URL}/{create_client.id}/balance")
    assert response.status_code == 400
    assert response.json() == {"detail": "The customer has no movement"}
