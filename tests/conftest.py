import pytest
from helpers import register_new_courier_and_return_login_password
from api_methods import ApiMethodsCourier


@pytest.fixture
def courier():
    data_create_courier = register_new_courier_and_return_login_password()
    ApiMethodsCourier.create_courier(data_create_courier)
    yield data_create_courier
    login = data_create_courier['login']
    password = data_create_courier['password']
    id_response = ApiMethodsCourier.login_courier(login, password)
    courier_id = id_response.json().get('id')
    ApiMethodsCourier.delete_courier(courier_id)