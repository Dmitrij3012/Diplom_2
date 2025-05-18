import allure
from methods.user_methods import UserMethods


class TestLogin:

    @allure.title('Успешное авторизация пользователя')
    @allure.description('Тест проверяет успешную авторизацию пользователя с валидными учетными данными.')
    def test_successful_login(self, create_user):

        with allure.step('Создание пользователя'):
            UserMethods.registration_user(create_user)

        with allure.step('Авторизация пользователя'):
            response = UserMethods.login_user(create_user)

        with allure.step('Проверка ответа'):
            assert response.status_code == 200
            assert response.json()['success'] is True
            assert 'accessToken' in response.text

    @allure.title('Ошибка авторизации при некорректном логине')
    @allure.description('Тест проверяет возврат ошибки при попытке авторизации с некорректным логином.')
    def test_error_with_incorrect_login(self, create_user):

        with allure.step('Создание пользователя'):
            UserMethods.registration_user(create_user)

        with allure.step('Авторизация пользователя'):
            body = {
                'email': 'qwerty',
                'password': create_user['password'],
            }
            response = UserMethods.login_user(body)

        with allure.step('Проверка ответа'):
            assert response.status_code == 401
            assert response.json()['success'] is False
            assert response.json()['message'] == 'email or password are incorrect'

    @allure.title('Ошибка авторизации при некорректном пароле')
    @allure.description('Тест проверяет возврат ошибки при попытке авторизации с некорректным паролем.')
    def test_error_with_incorrect_password(self, create_user):

        with allure.step('Создание пользователя'):
            UserMethods.registration_user(create_user)

        with allure.step('Авторизация пользователя'):
            body = {
                'email': create_user['email'],
                'password': 'qwerty',
            }
            response = UserMethods.login_user(body)

        with allure.step('Проверка ответа'):
            assert response.status_code == 401
            assert response.json()['success'] is False
            assert response.json()['message'] == 'email or password are incorrect'
