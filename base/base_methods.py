from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Base:
    """Base class containing generic methods"""
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

    input_email = "//input[@id='email']"
    input_password = "//input[@id='password']"
    button_submit = "//button[@type='submit']"
    user_for_test = "//div[contains(text(), 'Alexander')]"
    url = 'https://dev.clearbuy.com/login'

    def open_site(self):
        """Opening the main page"""
        self.driver.get(self.url)
        self.driver.maximize_window()

    def input_email_form(self, email):
        """Entering email"""
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_email))).send_keys(email)

    def input_password_form(self, password):
        """Entering password"""
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.input_password))).send_keys(password)

    def click_submit(self):
        """Clicking the login button"""
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_submit))).click()

    def get_logged_user(self):
        """Retrieving the username after login"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_for_test)))

    def authorization(self, email="alexyankovskio@gmail.com", password="qweQwe123#",
                      expected_username="Alexander Yankovsky"):
        """Logging into the system"""
        self.open_site()
        self.input_email_form(email)
        self.input_password_form(password)
        self.click_submit()
        user_element = self.get_logged_user()
        self.assert_word(user_element, expected_username)
