import pytest

from api.client import order_base_client
from resources.prepare_data import prepare_data
from helpers.models import delete_fields, parametrize_list_of_objects
from serializers.orders import Order


fields_to_test = parametrize_list_of_objects(Order)


@pytest.mark.parametrize('model, path', fields_to_test)
def test_optional_fields(model, path):

    # подготавливаем тестовые данные
    order = prepare_data('create_order')
    # удаляем обязательные атрибуты
    delete_fields('optional', order, model, path)

    # отправляем запрос на создание заказа
    create_order = order_base_client.create_order(order)

    # проверяем успешный код ответа и признак создания сущности
    assert create_order.status_code == 201, f'{create_order.text}'
    assert type(create_order.json()['id']) is int
