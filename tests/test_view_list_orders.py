import requests
from curl import list_order_api
import allure
from data import StatusCode


class TestListOrders:
    @allure.title("Проверка, что в теле ответа есть список заказов")
    def test_view_list_orders(self):
        response = requests.get(list_order_api)
        assert response.status_code == StatusCode.status_code_200 and 'orders' in response.text
