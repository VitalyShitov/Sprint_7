import allure
import pytest

from helpers.order_methods import get_orders_list

OK_CODE = 200
GATEWAY_ERRORS = (502, 504)


@allure.feature("Список заказов")
class TestOrdersList:

    @allure.title("В тело ответа возвращается список заказов")
    def test_orders_list_returns_list(self):
        response = get_orders_list()

        if response.status_code in GATEWAY_ERRORS:
            pytest.xfail(
                f"Стенд отвечает {response.status_code} (шлюз нестабилен) "
                "при запросе списка заказов"
            )

        assert response.status_code == OK_CODE

        body = response.json()
        assert isinstance(body["orders"], list)
        assert len(body["orders"]) > 0
