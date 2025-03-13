import requests
from curl import list_order_api
import allure

class TestListOrders:
    @allure.title("Проверка, что в теле ответа есть список заказов")
    def test_view_list_orders(self):
        response = requests.get(list_order_api)
        assert response.status_code == 200 and 'orders' in response.text
