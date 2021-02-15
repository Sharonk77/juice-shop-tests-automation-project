from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import uuid
from Repositories.Browser import Browser


class RegisterPage:
    EMAIL_FIELD = (By.ID, 'emailControl')
    ERROR_MESSAGE_CLASS_NAME = (By.CLASS_NAME, 'mat-error')
    VALIDATION_ERROR_CLASS_NAME = (By.CLASS_NAME, 'error')
    PASSWORD_FIELD = (By.ID, 'passwordControl')
    PASSWORD_REPEAT_FIELD = (By.ID, 'repeatPasswordControl')
    SECURITY_QUESTION_DROP_DOWN = (By.CLASS_NAME, 'mat-form-field-infix')
    SECURITY_QUESTION_MOVIE_OPTION = (By.CLASS_NAME, 'mat-option-text')
    SECURITY_QUESTION_ANSWER = (By.ID, 'securityAnswerControl')
    REGISTER_BUTTON = (By.ID, 'registerButton')
    TRANSLATE_POP_UP_MESSAGE = (By.ID, 'cdk-overlay-0')

    def __init__(self):
        self.browser = Browser.get_browser()
        self.browser.get("https://sharonkrochkovich.herokuapp.com/#/register")
        self.browser.maximize_window()
        pop_up_message = self.browser.find_elements_by_xpath(
            '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
        if len(pop_up_message) >= 1:
            pop_up_message[0].click()
        WebDriverWait(self.browser, 20).until(EC.invisibility_of_element_located((self.TRANSLATE_POP_UP_MESSAGE)))

    def kill_browser(self):
        Browser().kill_browser()

    def set_email(self, email=None):
        email_field = self.browser.find_element(*self.EMAIL_FIELD)
        email_field.send_keys(email if email is not None else f"{uuid.uuid4().hex}@gmail.com")

    def set_password(self, password=None, password_repeat=None):
        valid_password = "1" * 8
        password_field = self.browser.find_element(*self.PASSWORD_FIELD)
        password_field.send_keys(password if password is not None else f"{valid_password}")
        password_repeat_field = self.browser.find_element(*self.PASSWORD_REPEAT_FIELD)
        password_repeat_field.send_keys(password_repeat if password_repeat is not None else f"{valid_password}")

    def set_security_question(self):
        security_question_drop_down = self.browser.find_elements(*self.SECURITY_QUESTION_DROP_DOWN)
        security_question_drop_down[4].click()
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_all_elements_located(self.SECURITY_QUESTION_MOVIE_OPTION))
        security_questions = self.browser.find_elements(*self.SECURITY_QUESTION_MOVIE_OPTION)
        security_questions[11].click()

    def set_security_answer(self, answer=None):
        WebDriverWait(self.browser, 90).until(EC.presence_of_element_located((self.SECURITY_QUESTION_ANSWER)))
        security_question_answer = self.browser.find_element(*self.SECURITY_QUESTION_ANSWER)
        security_question_answer.send_keys(answer if answer is not None else "Movie")

    def click_register_button(self,wait_to_be_clickable=False):
        if wait_to_be_clickable is True:
            WebDriverWait(self.browser, 100).until(EC.element_to_be_clickable((self.REGISTER_BUTTON)))
        register_button = self.browser.find_element(*self.REGISTER_BUTTON)
        register_button.click()

    def get_current_url(self):
        return self.browser.current_url

    def get_error_message(self, error_message):
        WebDriverWait(self.browser, 20).until(EC.text_to_be_present_in_element(self.ERROR_MESSAGE_CLASS_NAME, error_message))
        return self.browser.find_element(*self.ERROR_MESSAGE_CLASS_NAME).text

    def get_all_error_messages(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_all_elements_located(self.ERROR_MESSAGE_CLASS_NAME))
        elements = self.browser.find_elements(*self.ERROR_MESSAGE_CLASS_NAME)
        return list(map(lambda item: item.text, elements))

    def get_api_validation_error(self, error_message):
        WebDriverWait(self.browser, 20).until(EC.text_to_be_present_in_element(self.VALIDATION_ERROR_CLASS_NAME, error_message))
        return self.browser.find_element(*self.VALIDATION_ERROR_CLASS_NAME).text

    def wait_for_url_to_contain_login(self):
        WebDriverWait(self.browser, 100).until(EC.url_contains('login'))

