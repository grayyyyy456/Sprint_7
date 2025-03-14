import pytest
import requests
from curl import creating_courier_api, delete_courier_api, login_courier_api
from helpers import register_new_courier_and_return_login_password

@pytest.fixture
def courier():
    data_create_courier = register_new_courier_and_return_login_password()
    response = requests.post(creating_courier_api, json=data_create_courier)
    assert response.status_code == 201 and response.json() == {"ok": True}
    yield data_create_courier
    login = data_create_courier['login']
    password = data_create_courier['password']
    id_response = requests.post(login_courier_api, json={'login': login, 'password': password})
    courier_id = id_response.json().get('id')
    delete_response = requests.delete(f"{delete_courier_api}/{courier_id}", json={"id": courier_id})
    assert response.json() == {"ok": True}