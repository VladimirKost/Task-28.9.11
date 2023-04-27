import requests

class OrderBaseClient:
    url = "https://some.url"

    def create_order(self, order):
        # Создание заказа
        return requests.post(self.url + '/orders', json=order)

    def delete_order(self):
        # Получить список всех заказов
        return requests.get(self.url + f'/orders/my_orders')

    def get(self, order_id):
        # Получение заказа
        return requests.get(self.url + f'/orders/{order_id}')

    def update(self, order_id):
        # Обновление заказа
        return requests.post(self.url + f'/orders/{order_id}')

    def delete_order(self, order_id):
        # Удаление заказа
        return requests.delete(self.url + f'/orders/{order_id}')


order_base_client = OrderBaseClient()
