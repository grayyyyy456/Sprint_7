import requests
from data import DataCourier
from curl import creating_courier_api
import allure

class TestCreateCourier:
    @allure.title("Проверка на создание курьера")
    def test_create_courier(self, courier):
        assert courier['login'] is not None
        assert courier['password'] is not None
        assert courier['firstName'] is not None

    @allure.title("Проверка на ошибку, при попытке создать двух одинаковых курьера")
    def test_create_two_identical_couriers(self, courier):
        data_create_courier = courier
        response = requests.post(creating_courier_api, json=data_create_courier)
        assert response.status_code == 409 and 'Этот логин уже используется. Попробуйте другой.' in response.text

    @allure.title("Проверка на ошибку, при создании курьера без логина")
    def test_create_courier_without_login(self):
        data_without_login = {"password": DataCourier.password}
        response = requests.post(creating_courier_api, json=data_without_login)
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title("Проверка на ошибку, при создании курьера без пароля")
    def test_create_courier_without_password(self):
        data_without_password = {"login": DataCourier.login}
        response = requests.post(creating_courier_api, json=data_without_password)
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.text





