import unittest
from Repositories.API.Register_endpoint import RegisterEndpoint
from Models.User_Data import UserData

class APItests(unittest.TestCase):
    def setUp(self):
        self.registration_endpoint = RegisterEndpoint()
        self.valid_data = UserData().user_data_generator()

    def test_successful_registration(self):
        result = self.registration_endpoint.send_post_request(data=self.valid_data)
        self.assertEqual(201, result.status_code, msg=result.content)
