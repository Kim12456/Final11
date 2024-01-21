#Василевская Екатерина, 12-я когорта - финальный проект. Инженер по тестированию плюс

import data_for_order
import sender_stand_request

# создание заказа и получение его номера
def get_new_order():
    new_order = data_for_order.order_body
    response = sender_stand_request.post_new_order(new_order)
    return response.json()["track"]

# сохранение номера заказа и получение заказа по треку заказа
def get_order_track():
    track = get_new_order()
    response = sender_stand_request.get_track(track)
    return response.json()

#Проверить, что код ответа равен 200
def test_status():
    assert get_order_track().status_code == 200








