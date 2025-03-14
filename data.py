class DataCourier:
    login = "gray1313"
    password = "1234"
    firstName = "sergio"
    id = "481450"

class StatusCode:
    status_code_200 = 200
    status_code_201 = 201
    status_code_400 = 400
    status_code_404 = 404
    status_code_409 = 409

class ResponseTextCreateCourier:
    text_status_code_201 = {"ok": True}
    text_status_code_400 = 'Недостаточно данных для создания учетной записи'
    text_status_code_409 = 'Этот логин уже используется. Попробуйте другой.'

class ResponseTextCreateOrder:
    text_status_code_201 = 'track'

class ResponseTextLoginCourier:
    text_status_code_200 = {'id': int(DataCourier.id)}
    text_status_code_400 = 'Недостаточно данных для входа'
    text_status_code_404 = 'Учетная запись не найдена'

class ResponseTextListOrder:
    text_status_code_200 = 'orders'