import configuration
import requests
import data_for_order

# создание заказа
def post_new_order(body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
	                     json = body)

# получить заказ по его номеру
def get_track(track):
	return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK + str(track),
						json = body)
