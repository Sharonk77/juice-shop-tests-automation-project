import unittest
from Models.Register_Page import RegisterPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import uuid

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

    def test_registration_with_wrong_email_null(self):
        self.register_page_handler.set_password()
        self.register_page_handler.set_security_question()
        self.register_page_handler.set_security_answer()
        self.register_page_handler.click_register_button(wait_to_be_clickable=False)
        WebDriverWait(self.register_page_handler.browser, 100).until(EC.url_contains('register'))
        url = self.register_page_handler.get_current_url()
        self.assertEqual(url, 'https://sharonkrochkovich.herokuapp.com/#/register')

    def test_registration_with_wrong_email_empty_string(self):
        self.register_page_handler.set_email(email='')
        self.register_page_handler.set_password()
        self.register_page_handler.set_security_question()
        self.register_page_handler.set_security_answer()
        self.register_page_handler.click_register_button(wait_to_be_clickable=False)
        error_message = self.register_page_handler.get_error_message('Please provide an email address.')
        self.assertEqual(error_message, 'Please provide an email address.')

    def test_registration_with_wrong_email_not_valid(self):
        self.register_page_handler.set_email(email=f"{uuid.uuid4().hex}#gmail.com")
        self.register_page_handler.set_password()
        self.register_page_handler.set_security_question()
        self.register_page_handler.set_security_answer()
        self.register_page_handler.click_register_button(wait_to_be_clickable=False)
        error_message = self.register_page_handler.get_error_message('Email address is not valid.')
        self.assertEqual(error_message, 'Email address is not valid.')

    def test_registration_with_wrong_password_4_digits(self):
        invalid_password = "1" * 4
        self.register_page_handler.set_email()
        self.register_page_handler.set_password(password=invalid_password, password_repeat=invalid_password)
        self.register_page_handler.set_security_question()
        self.register_page_handler.set_security_answer()
        self.register_page_handler.click_register_button(wait_to_be_clickable=False)
        error_message = self.register_page_handler.get_error_message('Password must be 5-20 characters long.')
        self.assertEqual(error_message, 'Password must be 5-20 characters long.')

    def test_registration_with_wrong_password_21_digits(self):
        invalid_password = "1" * 21
        self.register_page_handler.set_email()
        self.register_page_handler.set_password(password=invalid_password, password_repeat=invalid_password)
        self.register_page_handler.set_security_question()
        self.register_page_handler.set_security_answer()
        self.register_page_handler.click_register_button(wait_to_be_clickable=False)
        error_message = self.register_page_handler.get_error_message('Password must be 5-20 characters long.')
        self.assertEqual(error_message, 'Password must be 5-20 characters long.')
