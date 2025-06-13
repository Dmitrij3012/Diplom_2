import allure
import pytest
import data
from methods.user_methods import UserMethods


class TestCreateUser:

    @allure.title('Успешное создание пользователя')
    @allure.description('Создаем пользователя и проверяем успешность создания')
    def test_create_user(self, create_user):

        with allure.step('Создание пользователя'):
            response = UserMethods.registration_user(create_user)

        with allure.step('Проверка ответа'):
            assert response.status_code == 200
            assert response.json()['success'] is True

    @allure.title('Ошибка при создании двух одинаковых пользователей')
    @allure.description('Пытаемся создать двух одинаковых пользователей и получаем ошибку')
    def test_error_its_impossible_to_create_two_identical_user(self, create_user):

        with allure.step('Создание пользователя'):
            UserMethods.registration_user(create_user)

        with allure.step('Повторное создание пользователя'):
            response = UserMethods.registration_user(create_user)

        with allure.step('Проверка ответа'):
            assert response.status_code == 403
            assert response.json()['success'] is False
            assert response.json()['message'] == 'User already exists'

    @allure.title('Невозможность создания пользователя с пропущенным полем')
    @allure.description('Пытаемся создать пользователя с пропущенным полем и получаем ошибку')
    @pytest.mark.parametrize('body, status_code, success, response_text', data.BODY_WITH_EMPTY_FIELD)
    def test_error_if_one_of_the_fields_is_missing(self, body, status_code, success, response_text):

        with allure.step('Создание пользователя'):
            response = UserMethods.registration_user(body)

        with allure.step('Проверка ответа'):
            assert response.status_code == status_code
            assert response.json()['success'] is success
            assert response.json()['message'] == response_text
