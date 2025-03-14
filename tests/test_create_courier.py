from data import DataCourier, StatusCode, ResponseTextCreateCourier
import allure
from api_methods import ApiMethodsCourier

class TestCreateCourier:
    @allure.title("Проверка на создание курьера")
    def test_create_courier(self, courier):
        assert courier['login'] is not None
        assert courier['password'] is not None
        assert courier['firstName'] is not None

    @allure.title("Проверка на ошибку, при попытке создать двух одинаковых курьера")
    def test_create_two_identical_couriers(self, courier):
        data_create_courier = courier
        response = ApiMethodsCourier.create_courier(data_create_courier)
        assert response.status_code == StatusCode.status_code_409 and ResponseTextCreateCourier.text_status_code_409 in response.text

    @allure.title("Проверка на ошибку, при создании курьера без логина")
    def test_create_courier_without_login(self):
        data_without_login = {"password": DataCourier.password}
        response = ApiMethodsCourier.create_courier_without_login(data_without_login)
        assert response.status_code == StatusCode.status_code_400 and ResponseTextCreateCourier.text_status_code_400 in response.text

    @allure.title("Проверка на ошибку, при создании курьера без пароля")
    def test_create_courier_without_password(self):
        data_without_password = {"login": DataCourier.login}
        response = ApiMethodsCourier.create_courier_without_password(data_without_password)
        assert response.status_code == StatusCode.status_code_400 and ResponseTextCreateCourier.text_status_code_400 in response.text





