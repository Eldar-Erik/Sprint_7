import allure
import requests
from src.urls import PAGE_LOGIN_COURIER
from src.data import *
from src.request import new_login_data


class TestCreateLogin:

    @allure.title('Курьер может авторизоваться')
    def test_create_courier_success(self):
        payload = {"login": registrated_login,
                   "password": registrated_password
                   }
        response = requests.post(PAGE_LOGIN_COURIER, json=payload)
        assert response.status_code == 200

    @allure.title('Для авторизации нужно передать все обязательные поля')
    def test_login_required_field_false(self):
        payload = {"login": registrated_login,
                   "password": empty_field}
        response = requests.post(PAGE_LOGIN_COURIER, json=payload)
        assert response.status_code == 400

    @allure.title('Cистема вернёт ошибку, если неправильно указать логин или пароль')
    def test_login_wrong_data_false(self):
        new_data = new_login_data()
        response = requests.post(PAGE_LOGIN_COURIER, json=new_data)
        assert response.status_code == 404

    @allure.title('Если какого-то поля нет, запрос возвращает ошибку')
    def test_login_required_field_error_success(self):
        payload = {"login": registrated_login,
                   "password": empty_field}
        response = requests.post(PAGE_LOGIN_COURIER, json=payload)
        assert response.json().get("message") == "Недостаточно данных для входа"

    @allure.title('Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_login_wrong_data_error_success(self):
        new_data = new_login_data()
        response = requests.post(PAGE_LOGIN_COURIER, json=new_data)
        assert response.json().get("message") == "Учетная запись не найдена"

    @allure.title('Успешный запрос возвращает id')
    def test_create_courier_success(self):
        payload = {"login": registrated_login,
                   "password": registrated_password
                   }
        response = requests.post(PAGE_LOGIN_COURIER, json=payload)
        assert response.json()['id']
