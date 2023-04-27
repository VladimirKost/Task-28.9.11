from api.client import order_base_client, OrderBaseClient
from resources.prepare_data import prepare_data

    # 1
    """Проверяем возможность вызвать список заказов, 1+ заказов должны отображаться в списке"""
def test_myl():
    # подготавливаем тестовые данные
    order = prepare_data('create_order')
    # создаем тестовый заказ
    create_order = order_base_client.create_order(order)
    # вызываем общий список заказов
    my_orders = requests.get(self.url + f'/orders/my_orders')

    assert my_orders.status_code == 200
    assert len(my_orders) >= 1
    assert create_order['id'] in my_orders

    # 2
    """Проверяем возможность удалить заказ"""
def test_delete_order():
    # подготавливаем тестовые данные
    order = prepare_data('create_order')
    # создаем заказ
    create_order = order_base_client.create_order(order)
    # получаем его id для получения
    order_id = create_order.json()['id']

    # пробуем удалить созданный заказ
    delete_order = requests.delete(self.url + f'/orders/{order_id}')
    my_orders = requests.get(self.url + f'/orders/my_orders')

    assert delete_order.status_code == 200, f'{delete_order.text}'
    assert delete_order['id'] not in my_orders

    # 3
    """Проверяем невозможность удалить случайный заказ"""
def test_delete_random_order():
    my_orders = requests.get(self.url + f'/orders/my_orders')
    # изымаем случайный заказ из списка
    order_id = my_orders.json()[0]

    # пробуем удалить заказ
    delete_order = requests.delete(self.url + f'/orders/{order_id}')

    assert delete_order.status_code == 400
    assert Exception("Provided data is incorrect")

    # 4
    """Проверяем возможность обновить заказ"""
def test_update_order(order='1', model='Боди', path='г. N'):
    # подготавливаем тестовые данные
    order = prepare_data('create_order')
    # создаем заказ
    create_order = order_base_client.create_order(order)
    # получаем его id для получения
    order_id = create_order.json()['id']
    # пробуем обновить информацию
    update_order = requests.post(self.url + f'/orders/{order_id}', headers=(order='1', model='Боди', path='г. N'))


    assert update_order.status_code == 200
    assert  result['headers'] = headers

    # 5
    """Проверяем возможность отобразить пустой список заказов"""
def test_empty_ml():
    # вызываем общий список заказов
    my_orders = requests.get(self.url + f'/orders/my_orders')

    assert my_orders.status_code == 200
    assert len(my_orders) == 0

    # 6
    """Проверяем невозможность удалить чужой заказ"""
def test_delete_foreign_order():
    # изымаем случайный заказ из списка
    order_id = order_base_client.json()[0]

    # пробуем удалить заказ
    delete_order = requests.delete(self.url + f'/orders/{order_id}')

    assert delete_order.status_code == 403
    assert Exception("Invalid auth key attempted for this user")

    # 7
    """Проверяем невозможность обновить заказ на пустые поля"""
def test_update_order():
    # подготавливаем тестовые данные
    order = prepare_data('create_order')
    # создаем заказ
    create_order = order_base_client.create_order(order)
    # получаем его id для получения
    order_id = create_order.json()['id']
    # пробуем обновить информацию
    update_order = requests.post(self.url + f'/orders/{order_id}', headers=(order=' ', model=' ', path=' '))

    assert update_order.status_code == 400
    assert Exception("Provided data is incorrect")