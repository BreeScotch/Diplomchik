# Андрей Шушков, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data
# запрос на создание заказа.
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)
# сохраняем номер трека заказа.
response = post_new_order()
track = response.json()["track"]

# запрос на получение заказа по треку заказа.
def get_order_info(track):
  return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO_PATH, params={"t": track})
response = get_order_info(track)

# Проверить, что код ответа равен 200
if response.status_code == 200:
  print("Тест пройден")
else:
  print(f"Тест провален: {response.status_code}")
