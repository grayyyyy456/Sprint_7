import pytest
from api_methods import ApiMethodsOrder
import allure
from data import StatusCode, ResponseTextCreateOrder


class TestCreateOrder:
    @allure.title("Проверка выбора разных цветом самоката при заказе")
    @pytest.mark.parametrize("firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color",[
        ("Sergio", "Ramas", "Усачева, 3", 4, "+79001234567", 3, "2025-03-13", "хочу черный", ['BLACK']),
        ("Sergio", "Ramas", "Усачева, 3", 4, "+79001234567", 3, "2025-03-13", "хочу серый", ['GREY']),
        ("Sergio", "Ramas", "Усачева, 3", 4, "+79001234567", 3, "2025-03-13", "не знаю, какой хочу", ['GREY', 'BLACK']),
        ("Sergio", "Ramas", "Усачева, 3", 4, "+79001234567", 3, "2025-03-13", "цвет?", None),
        ("Sergio", "Ramas", "Усачева, 3", 4, "+79001234567", 3, "2025-03-13", "хочу любой", "")])
    def test_create_order(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": color
        }
        response = ApiMethodsOrder.create_order(payload)
        assert response.status_code == StatusCode.status_code_201 and ResponseTextCreateOrder.text_status_code_201 in response.json()
