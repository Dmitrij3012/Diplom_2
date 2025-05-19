import requests
import url


class UserMethods:

    @staticmethod
    def registration_user(body):
        return requests.post(f'{url.REGISTRATION}', json=body)

    @staticmethod
    def login_user(body):
        return requests.post(f'{url.LOGIN}', json=body)

    @staticmethod
    def changing_user_data(body, token):
        return requests.patch(f'{url.USER}', json=body, headers={'Authorization': token})

    @staticmethod
    def delete_user(token):
        return requests.delete(f'{url.DELETE}', headers={'Authorization': token})
