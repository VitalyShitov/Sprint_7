import allure

import helpers.order as order_helper

OK_CODE = 200


@allure.feature("Список заказов")
class TestOrdersList:

    @allure.story("В тело ответа возвращается список заказов")
    def test_orders_list_returns_list(self):
        response = order_helper.get_orders_list()
        assert response.status_code == OK_CODE

        body = response.json()
        assert isinstance(body["orders"], list)
        assert len(body["orders"]) > 0
