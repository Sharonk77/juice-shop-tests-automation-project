import unittest
from Repositories.API.Register_endpoint import RegisterEndpoint
from Models.User_Data import UserData
import uuid

class APItests(unittest.TestCase):
    def setUp(self):
        self.registration_endpoint = RegisterEndpoint()
        self.valid_data = UserData().user_data_generator()

    def test_successful_registration(self):
        result = self.registration_endpoint.send_post_request(data=self.valid_data)
        self.assertEqual(201, result.status_code, msg=result.content)

    def test_registration_with_existing_email(self):
        self.valid_data["email"] = "test@gmail.com"
        result = self.registration_endpoint.send_post_request(data=self.valid_data)
        self.assertNotEqual(201, result.status_code, result.content)

    def test_registration_with_wrong_email_null(self):
        self.valid_data["email"] = None
        result = self.registration_endpoint.send_post_request(data=self.valid_data)
        self.assertNotEqual(201, result.status_code, result.content)

    def test_registration_with_wrong_email_empty_string(self):
        self.valid_data["email"] = ''
        result = self.registration_endpoint.send_post_request(data=self.valid_data)
        self.assertNotEqual(201, result.status_code, result.content)

    def test_registration_with_wrong_email_not_valid(self):
        self.valid_data["email"] = f"{uuid.uuid4().hex}#gmail.com"
        result = self.registration_endpoint.send_post_request(data=self.valid_data)
        self.assertNotEqual(201, result.status_code, result.content)

    def test_registration_with_wrong_password_4_digits(self):
        self.valid_data["password"] = '1' * 4
        result = self.registration_endpoint.send_post_request(data=self.valid_data)
        self.assertNotEqual(201, result.status_code, result.content)

    def test_registration_with_wrong_password_21_digits(self):
        self.valid_data["password"] = '1' * 21
        result = self.registration_endpoint.send_post_request(data=self.valid_data)
        self.assertNotEqual(201, result.status_code, result.content)

    def test_registration_with_wrong_password_null(self):
        self.valid_data["password"] = None
        result = self.registration_endpoint.send_post_request(data=self.valid_data)
        self.assertNotEqual(201, result.status_code, result.content)

    def test_registration_with_wrong_password_empty_string(self):
        self.valid_data["password"] = ''
        result = self.registration_endpoint.send_post_request(data=self.valid_data)
        self.assertNotEqual(201, result.status_code, result.content)

    def test_registration_with_wrong_repeated_password(self):
        self.valid_data["passwordRepeat"] = "11111111"
        result = self.registration_endpoint.send_post_request(data=self.valid_data)
        self.assertNotEqual(201, result.status_code, result.content)

