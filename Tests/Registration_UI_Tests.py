import unittest
from Models.Register_Page import RegisterPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class UItests(unittest.TestCase):

    def setUp(self):
        self.register_page_handler = RegisterPage()

    def tearDown(self):
        self.register_page_handler.kill_browser()

    def test_successful_registration(self):
        self.register_page_handler.set_email()
        self.register_page_handler.set_password()
        self.register_page_handler.set_security_question()
        self.register_page_handler.set_security_answer()
        self.register_page_handler.click_register_button()
        WebDriverWait(self.register_page_handler.browser, 100).until(EC.url_contains('login'))
        url = self.register_page_handler.get_current_url()
        self.assertEqual(url, 'https://sharonkrochkovich.herokuapp.com/#/login')

    def test_registration_with_existing_email(self):
        self.register_page_handler.set_email(email='test@gmail.com')
        self.register_page_handler.set_password()
        self.register_page_handler.set_security_question()
        self.register_page_handler.set_security_answer()
        self.register_page_handler.click_register_button()
        error_message = self.register_page_handler.get_api_validation_error('Email must be unique')
        self.assertEqual(error_message, 'Email must be unique')
