from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from utilities.logger import Logger


class Base:
    """Base class containing generic methods"""
    INPUT_EMAIL = "//input[@id='email']"
    INPUT_PASSWORD = "//input[@id='password']"
    BUTTON_SUBMIT = "//button[@type='submit']"
    USER_FOR_TEST = "//div[contains(text(), 'Alexander')]"
    URL = 'https://dev.clearbuy.com/login'

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """URL check method"""
        get_url = self.driver.current_url
        print("current url " + get_url)

    def assert_url(self, result):
        """Checking the correctness of the URL"""
        get_url = self.driver.current_url
        print(get_url)
        assert result == get_url
        print("--URL is correct--")

    def assert_word(self, word, result):
        """Checking the text"""
        value_word = word.text
        assert value_word == result
        print(f"Text {value_word} matches the {result}")

    def scroll_down(self, pixels=1000):
        """Scrolls the page down by a specified number of pixels"""
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        print(f"Page scrolled down by {pixels} pixels")

    # ==== Methods for authorization ====

    def open_site(self):
        """Opening the main page"""
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def input_email_form(self, email):
        """Entering email"""
        WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable((By.XPATH, self.INPUT_EMAIL))) \
            .send_keys(email)

    def input_password_form(self, password):
        """Entering password"""
        WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable((By.XPATH, self.INPUT_PASSWORD))) \
            .send_keys(password)

    def click_submit(self):
        """Clicking the login button"""
        WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable((By.XPATH, self.BUTTON_SUBMIT))) \
            .click()

    def get_logged_user(self):
        """Retrieving the username after login"""
        return WebDriverWait(self.driver, 30) \
            .until(EC.element_to_be_clickable((By.XPATH, self.USER_FOR_TEST)))

    def authorization(self, email="alexyankovskio@gmail.com", password="qweQwe123#",
                      expected_username="Alexander Yankovsky"):
        """Logging into the system"""
        Logger.add_start_step(method="authorization")
        self.open_site()
        self.input_email_form(email)
        self.input_password_form(password)
        self.click_submit()
        user_element = self.get_logged_user()
        self.assert_word(user_element, expected_username)
        Logger.add_end_step(url=self.driver.current_url, method="authorization")

