import allure

import data
from methods.user_methods import UserMethods


class TestChangingUserData:

    @allure.title('Успешное изменение данных пользователя')
    @allure.description('Тест проверяет успешное изменение данных пользователя.')
    def test_successful_changing_data(self, create_user_with_token):

        with allure.step('Создание пользователя и авторизация'):
            UserMethods.registration_user(create_user_with_token)

        with allure.step('Получение токена'):
            token = create_user_with_token

        with allure.step('Изменение данных'):
            body = {
                'email': 'qwerty777@test123123.com',
                'password': 'QWERTY7771234',
                'name': '1234'
            }
            response = UserMethods.changing_user_data(body, token)

        with allure.step('Проверка ответа'):
            assert response.status_code == 200
            assert response.json()['success'] is True
            assert response.json()['user']['email'] == 'qwerty777@test123123.com'
            assert response.json()['user']['name'] == '1234'

    @allure.title('Ошибка изменения данных пользователя без авторизации')
    @allure.description('Тест проверяет возврат ошибки при попытке изменения данных пользователя без авторизации')
    def test_error_changing_data_without_login(self, create_user_with_token):

        with allure.step('Создание пользователя и авторизация'):
            UserMethods.registration_user(create_user_with_token)

        with allure.step('Пустой токен'):
            token = ''

        with allure.step('Изменение данных'):
            body = data.MODIFIED_DATA
            response = UserMethods.changing_user_data(body, token)

        with allure.step('Проверка ответа'):
            assert response.status_code == 401
            assert response.json()['success'] is False
            assert response.json()['message'] == 'You should be authorised'
