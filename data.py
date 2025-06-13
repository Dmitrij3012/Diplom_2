from generators import fake_data


class Data:

    @staticmethod
    def user_body():
        email, password, name = fake_data()
        return {
            'email': email,
            'password': password,
            'name': name
        }


BODY_WITH_EMPTY_FIELD = (
    ({
         'email': '',
         'password': Data.user_body()['password'],
         'name': Data.user_body()['name']
     }, 403, False, 'Email, password and name are required fields'),
    ({
         'email': Data.user_body()['email'],
         'password': '',
         'name': Data.user_body()['name']
     }, 403, False, 'Email, password and name are required fields'),
    ({
         'email': Data.user_body()['email'],
         'password': Data.user_body()['password'],
         'name': ''
     }, 403, False, 'Email, password and name are required fields')
)

ORDER = {
    'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa73']
}

INGREDIENTS = (
    ({
         'ingredients': ''
     }, 400, 'false', 'Ingredient ids must be provided'),
    ({
         'ingredients': ['1234', 'qwerty', '!@#$%']
     }, 500, 'Error', 'Internal Server Error')
)

MODIFIED_DATA = {
    'email': 'qwerty777@test123123.com',
    'password': 'QWERTY7771234',
    'name': '1234'
}
