import pytest
from data import Data
from methods.auth_methods import AuthMethods
from methods.user_methods import UserMethods


@pytest.fixture
def create_user():
    user_data = Data.user_body()
    yield user_data
    token = AuthMethods.get_tokens(user_data)
    UserMethods.delete_user(token)


@pytest.fixture
def create_user_with_token():
    user_data = Data.user_body()
    UserMethods.registration_user(user_data)
    token = AuthMethods.get_tokens(user_data)
    yield token
    UserMethods.delete_user(token)
