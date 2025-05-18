import requests
import url


class AuthMethods:

    @staticmethod
    def get_tokens(body):
        response = requests.post(f'{url.MAIN}{url.LOGIN}', json=body)
        return response.json()['accessToken']
