#Нюганен Юлия 22-я когорта дипломный проект

import sender_stand_request

#Функция для позитивной проверки
def positive_assert(track_orders):
# В переменную track_response сохраняем результат запроса на получение заказа по треку
    track_response = sender_stand_request.get_orders(track_orders)
# Проверяем, что код ответа равен 200
    assert track_response.status_code == 200


# Тест: проверяем, что по треку заказа можно получить данные о заказе
def test_get_orders_track_positive_response():
    positive_assert(sender_stand_request.track_orders)