from selenium.webdriver.common.by import By

from base.base_methods import BasePage
from utilities.logger import Logger

class LoginPageLocators:
    INPUT_EMAIL = (By.XPATH, "//input[@id='email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@id='password']")
    BUTTON_SUBMIT = (By.XPATH, "//button[@type='submit']")
    USER_FOR_TEST = (By.XPATH, "//div[contains(text(), 'Alexander')]")
    URL = 'https://dev.clearbuy.com/login'


class LoginPageGetters(BasePage):
    @staticmethod
    def assert_user_name():
        return LoginPageLocators.USER_FOR_TEST


class LoginPageActions(LoginPageGetters):
    def input_email_form(self):
        self.input_text(LoginPageLocators.INPUT_EMAIL, "alexyankovskio@gmail.com")

    def input_password_form(self):
        self.input_text(LoginPageLocators.INPUT_PASSWORD, "qweQwe123#")

    def click_submit_button(self):
        self.click_element(LoginPageLocators.BUTTON_SUBMIT)

class LoginPageSteps(LoginPageActions):
    def authorization(self):
        """Logging into the system"""
        Logger.add_start_step(method="authorization")
        self.open_site(LoginPageLocators.URL)
        self.input_email_form()
        self.input_password_form()
        self.click_submit_button()
        self.assert_word(self.assert_user_name(), "Alexander Yankovsky")
        Logger.add_end_step(url=self.driver.current_url, method="authorization")


