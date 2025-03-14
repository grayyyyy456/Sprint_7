import pytest
from helpers import register_new_courier_and_return_login_password
from data import ResponseTextCreateCourier, StatusCode, ResponseTextDeleteCourier
from api_methods import ApiMethodsCourier


@pytest.fixture
def courier():
    data_create_courier = register_new_courier_and_return_login_password()
    response = ApiMethodsCourier.create_courier(data_create_courier)
    assert response.status_code == StatusCode.status_code_201 and response.json() == ResponseTextCreateCourier.text_status_code_201
    yield data_create_courier
    login = data_create_courier['login']
    password = data_create_courier['password']
    id_response = ApiMethodsCourier.login_courier(login, password)
    courier_id = id_response.json().get('id')
    delete_response = ApiMethodsCourier.delete_courier(courier_id)
    assert delete_response.status_code == StatusCode.status_code_200 and response.json() == ResponseTextDeleteCourier.text_status_code_200