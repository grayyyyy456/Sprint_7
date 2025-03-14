import requests
from data import DataCourier, StatusCode, ResponseTextLoginCourier
from curl import login_courier_api
import allure
from api_methods import ApiMethodsCourier

class TestLoginCourier:
    @allure.title("Проверка что курьер может авторизороваться")
    def test_courier_authorization(self):
        data_create_courier = {
            'login': DataCourier.login,
            'password': DataCourier.password
        }
        response = ApiMethodsCourier.courier_authorization(data_create_courier)
        assert response.status_code == StatusCode.status_code_200 and response.json() == ResponseTextLoginCourier.text_status_code_200

    @allure.title("Проверка на ошибку, при авторизации без логина")
    def test_courier_authorization_without_login(self):
        data_create_courier = {'password': DataCourier.password}
        response = ApiMethodsCourier.courier_authorization(data_create_courier)
        assert response.status_code == StatusCode.status_code_400 and ResponseTextLoginCourier.text_status_code_400 in response.text

    @allure.title("Проверка на ошибку, при авторизации без пароля")
    def test_courier_authorization_without_password(self):   # падает с кодом 504
        data_create_courier = {'login': DataCourier.login}
        response = ApiMethodsCourier.courier_authorization(data_create_courier)
        assert response.status_code == StatusCode.status_code_400 and ResponseTextLoginCourier.text_status_code_400 in response.text

    @allure.title("Проверка на ошибку, при авторизации с ошибкой в пароле")
    def test_courier_authorization_with_wrong_password(self):
        data_create_courier = {
            'login': DataCourier.login,
            'password': DataCourier.password + 'a'
        }
        response = ApiMethodsCourier.courier_authorization(data_create_courier)
        assert response.status_code == StatusCode.status_code_404 and ResponseTextLoginCourier.text_status_code_404 in response.text

    @allure.title("Проверка на ошибку, при авторизации с ошибкой в логине")
    def test_courier_authorization_with_wrong_login(self):
        data_create_courier = {
            'login': DataCourier.login.upper(),
            'password': DataCourier.password
        }
        response = ApiMethodsCourier.courier_authorization(data_create_courier)
        assert response.status_code == StatusCode.status_code_404 and ResponseTextLoginCourier.text_status_code_404 in response.text


