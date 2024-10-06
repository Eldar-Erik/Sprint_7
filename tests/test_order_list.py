import allure
import requests
from src.urls import PAGE_ORDER_LIST


class TestOrderList:
    @allure.title('Тело ответа возвращается список заказов.')
    def test_order_list(self):
        response = requests.get(PAGE_ORDER_LIST)
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)
