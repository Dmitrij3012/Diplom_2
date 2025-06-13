import allure
import data
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


class TestGetOrder:

    @allure.title('Успешное получение списка заказов конкретного пользователя')
    @allure.description('Тест проверяет успешное получение списка заказов конкретного пользователя.')
    def test_success_get_order(self, create_user_with_token):

        with allure.step('Создание пользователя и авторизация'):
            UserMethods.registration_user(create_user_with_token)

        with allure.step('Получение токена'):
            token = create_user_with_token

        with allure.step('Создание заказа'):
            OrderMethods.create_order(data.ORDER, token)

        with allure.step('Получение списка заказов'):
            response = OrderMethods.get_order(token)

        with allure.step('Проверка ответа'):
            assert response.status_code == 200
            assert response.json()['success'] is True
            assert 'createdAt' in response.text

    @allure.title('Ошибка получения списка заказов конкретного пользователя без авторизации')
    @allure.description('Тест проверяет ошибку получения списка заказов конкретного пользователя без авторизации.')
    def test_error_get_order_without_registration(self):

        with allure.step('Получение списка заказов'):
            response = OrderMethods.get_order('')

        with allure.step('Проверка ответа'):
            assert response.status_code == 401
            assert response.json()['success'] is False
            assert response.json()['message'] == 'You should be authorised'
