import allure
import pytest
import data
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


class TestCreateOrder:

    @allure.title('Успешное создание заказа с авторизацией пользователя')
    @allure.description('Тест проверяет успешное создание заказа с авторизацией пользователя.')
    def test_successful_create_order(self, create_user_with_token):

        with allure.step('Создание пользователя и авторизация'):
            UserMethods.registration_user(create_user_with_token)

        with allure.step('Получение токена'):
            token = create_user_with_token

        with allure.step('Создание заказа'):
            response = OrderMethods.create_order(data.ORDER, token)

        with allure.step('Проверка ответа'):
            assert response.status_code == 200
            assert 'order' in response.text
            assert 'number' in response.text
            assert 'Space бессмертный флюоресцентный' in response.text
            assert response.json()['success'] is True

    @allure.title('Успешное создание заказа без авторизации пользователя')
    @allure.description('Тест проверяет успешное создание заказа без авторизации пользователя.')
    def test_error_create_order_without_registration(self):

        with allure.step('Создание заказа'):
            response = OrderMethods.create_order(data.ORDER, None)

        with allure.step('Проверка ответа'):
            assert response.status_code == 200
            assert 'order' in response.text
            assert 'number' in response.text
            assert response.json()['success'] is True

    @allure.title('Успешное создание заказа с ингредиентами')
    @allure.description('Тест проверяет успешное создание заказа с ингредиентами.')
    def test_successful_create_order_with_ingredients(self, create_user_with_token):
        with allure.step('Создание пользователя и авторизация'):
            UserMethods.registration_user(create_user_with_token)

        with allure.step('Получение токена'):
            token = create_user_with_token

        with allure.step('Создание заказа'):
            response = OrderMethods.create_order(data.ORDER, token)

        with allure.step('Проверка ответа'):
            assert response.status_code == 200
            assert 'order' in response.text
            assert 'number' in response.text
            assert 'Space бессмертный флюоресцентный' in response.text
            assert response.json()['success'] is True

    @allure.title('Ошибка создания заказа с некорректными ингредиентами')
    @allure.description('Тест проверяет ошибку создания заказа с некорректными ингредиентами.')
    @pytest.mark.parametrize('body, status_code, success, response_text', data.INGREDIENTS)
    def test_error_order_with_invalid_ingredients(self, create_user_with_token, body,
                                                  status_code, success, response_text):
        with allure.step('Создание пользователя и авторизация'):
            UserMethods.registration_user(create_user_with_token)

        with allure.step('Получение токена'):
            token = create_user_with_token

        with allure.step('Создание заказа'):
            response = OrderMethods.create_order(body, token)

        with allure.step('Проверка ответа'):
            assert response.status_code == status_code
            assert success in response.text
            assert response_text in response_text
