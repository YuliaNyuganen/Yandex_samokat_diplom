import configuration
import data
import requests

#Создаем новый заказ
def post_new_orders(orders_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=orders_body)
response = post_new_orders(data.orders_body)
print("КОД ОТВЕТА ДЛЯ НОВОГО заказа:" + str(response.status_code))
print("ТЕЛО ОТВЕТА ДЛЯ НОВОГО заказа:" + str(response.json()))

#Получаем трек номер
track_orders=response.json()["track"]

#Получаем заказ по номеру трека
def get_orders(track_orders):
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_TRACK,
                        params={"t": track_orders})
response= get_orders(track_orders)
print("КОД ОТВЕТА ДЛЯ заказа по номеру трека:" + str(response.status_code))
print("ТЕЛО ОТВЕТА ДЛЯ заказа по номеру трека:" + str(response.json()))