from api.client import order_base_client
from resources.prepare_data import prepare_data
from serializers.orders import Order


def test_base():
    # подготавливаем тестовые данные
    order = prepare_data('create_order')
    # создаем заказ
    create_order = order_base_client.create_order(order)
    # получаем его id для получения
    order_id = create_order.json()['id']

    # получаем созданный заказ из сервиса
    get_order = order_base_client.get_order(order_id)

    assert Order(**order).dict() == Order(**get_order.json()).dict()
    assert get_order.status_code == 204, f'{get_order.json()}'
    assert get_order.content == b''
