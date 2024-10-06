import allure
import requests
from src.urls import PAGE_CREATE_COURIER
from src.data import *
from src.request import new_courier_data


class TestCreateCourier:

    @allure.title('Курьера можно создать')
    def test_create_courier_success(self):
        new_courier = new_courier_data()
        response = requests.post(PAGE_CREATE_COURIER, json=new_courier)
        assert response.status_code == 201

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier_false(self):
        payload = {"login": registrated_login,
                   "password": registrated_password,
                   "firstName": registrated_firstName
                   }
        response = requests.post(PAGE_CREATE_COURIER, json=payload)
        assert response.status_code == 409

    @allure.title('Чтобы создать курьера, нужно передать в ручку все обязательные поля')
    def test_create_courier_whithout_login_false(self):
        payload = {"password": registrated_password,
                   "firstName": registrated_firstName
                   }
        response = requests.post(PAGE_CREATE_COURIER, json=payload)
        assert response.status_code == 400

    @allure.title('Запрос возвращает правильный код ответа')
    def test_create_courier_success_code(self):
        new_courier = new_courier_data()
        response = requests.post(PAGE_CREATE_COURIER, json=new_courier)
        assert response.status_code == 201

    @allure.title('Успешный запрос возвращает "ok":true')
    def test_create_courier_success_answer(self):
        new_courier = new_courier_data()
        response = requests.post(PAGE_CREATE_COURIER, json=new_courier)
        assert response.json() == {"ok": True}

    @allure.title('Если одного из полей нет, запрос возвращает ошибку')
    def test_create_courier_whithout_login_answer(self):
        payload = {"password": registrated_password,
                   "firstName": registrated_firstName
                   }
        response = requests.post(PAGE_CREATE_COURIER, json=payload)
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title('Если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_create_duplicate_courier_login_false(self):
        payload = {"login": registrated_login,
                   "password": registrated_password,
                   "firstName": registrated_firstName
                   }
        response = requests.post(PAGE_CREATE_COURIER, json=payload)
        assert response.status_code == 409
