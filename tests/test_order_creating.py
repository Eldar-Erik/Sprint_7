import pytest
import allure
import requests
from src.urls import PAGE_ORDER_CREATE
from src.request import order_data


class TestCreateOrder:
    @allure.title('Можно указать один из цветов — BLACK или GREY')
    @pytest.mark.parametrize('color', [(["BLACK"]), (["GREY"]), (["BLACK", "GREY"]), ([])])
    def test_create_courier_success(self, color):
        new_data = order_data(color)
        response = requests.post(PAGE_ORDER_CREATE, json=new_data)
        assert response.status_code == 201
        assert response.json()['track']
