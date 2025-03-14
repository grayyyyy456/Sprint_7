from api_methods import ApiMethodsOrder
import allure
from data import StatusCode, ResponseTextListOrder


class TestListOrders:
    @allure.title("Проверка, что в теле ответа есть список заказов")
    def test_view_list_orders(self):
        response = ApiMethodsOrder.order_list()
        assert response.status_code == StatusCode.status_code_200 and ResponseTextListOrder.text_status_code_200 in response.text
