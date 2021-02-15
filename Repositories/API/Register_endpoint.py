import requests


class RegisterEndpoint:

    def __init__(self):
        self.register_endpoint = "https://sharonkrochkovich.herokuapp.com/api/Users/"

    def send_post_request(self, data):
        r = requests.post(url=self.register_endpoint, json=data)
        return r
