import requests
from curl import creating_courier_api, login_courier_api, delete_courier_api, creating_order_api, list_order_api

class ApiMethodsCourier:
    @staticmethod
    def create_courier(data_create_courier):
        return requests.post(creating_courier_api, json=data_create_courier)

    @staticmethod
    def create_courier_without_login(data_without_login):
        return requests.post(creating_courier_api, json=data_without_login)

    @staticmethod
    def create_courier_without_password(data_without_password):
        return requests.post(creating_courier_api, json=data_without_password)

    @staticmethod
    def login_courier(login, password):
        return requests.post(login_courier_api, json={'login': login, 'password': password})

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f"{delete_courier_api}/{courier_id}", json={"id": courier_id})

    @staticmethod
    def courier_authorization(data_create_courier):
        return requests.post(login_courier_api, json=data_create_courier)

class ApiMethodsOrder:
    @staticmethod
    def create_order(payload):
        return requests.post(creating_order_api, json=payload)

    @staticmethod
    def order_list():
        return requests.get(list_order_api)

