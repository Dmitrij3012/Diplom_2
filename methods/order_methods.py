import requests
import url


class OrderMethods:

    @staticmethod
    def create_order(body, token):
        return requests.post(f'{url.ORDER}', json=body, headers={'Authorization': token})

    @staticmethod
    def get_order(token):
        return requests.get(f'{url.ORDER}', headers={'Authorization': token})
