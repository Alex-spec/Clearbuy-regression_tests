from pages.os_section import OsSection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure
from utilities.logger import Logger


class UserSection(OsSection):
    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS
    """Roles locators"""
    USERS = "//span[contains(text(), 'Users')]"
    ROLES = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[18]"
    NEW_ROLE = "//a[contains(text(), 'New Role')]"
    PERMISSION = "(//div[@class='mr-1 checkbox__control'])[1]"

    """Users locators"""
    USERS_TAB = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[19]"
    NEW_USER = "//a[contains(text(), 'New User')]"
    USER_NAME = "//input[@name='name']"
    EMAIL = "//input[@name='email']"
    PASSWORD = "//input[@name='password']"
    PASSWORD_CONFIRMATION = "//input[@name='password_confirmation']"
    ADMIN_ROLE = "(//div[@class='checkbox__control__indicator'])[1]"

    """Domains locators"""
    DOMAIN = "//a[contains(text(), 'Allowed auth domains')]"
    NEW_DOMAIN = "//a[contains(text(), 'Domain')]"
    DOMAIN_FIELD = "//input[@name='domain']"
    SELECT_DOMAIN = "(//input[@class='selectAllCheckable'])[1]"
    DELETE_DOMAIN = "//a[contains(text(), 'Delete Selected')]"
    DELETE_DOMAIN_CONFIRMATION = "//a[normalize-space(text()) = 'Delete']"

    # GETTERS
    """Roles getters"""
    def get_users(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.USERS)))

    def get_roles(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ROLES)))

    def get_new_role(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_ROLE)))

    def get_permission(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.PERMISSION)))

    """Users getters"""
    def get_users_tab(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.USERS_TAB)))

    def get_new_user(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_USER)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.USER_NAME)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.EMAIL)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.PASSWORD)))

    def get_password_confirmation(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.PASSWORD_CONFIRMATION)))

    def get_admin_role(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ADMIN_ROLE)))

    """Domains getters"""
    def get_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.DOMAIN)))

    def get_new_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_DOMAIN)))

    def get_domain_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.DOMAIN_FIELD)))

    def get_select_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.SELECT_DOMAIN)))

    def get_delete_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.DELETE_DOMAIN)))

    def get_delete_domain_confirmation(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.DELETE_DOMAIN_CONFIRMATION)))

    # ACTIONS
    """Roles actions"""
    def click_users(self):
        self.get_users().click()
        print("Clicked on the users section")

    def click_roles(self):
        self.get_roles().click()
        print("Clicked on the roles tab")

    def click_new_role(self):
        self.get_new_role().click()
        print("Clicked on the new role button")

    def click_permission(self):
        self.get_permission().click()
        print("Clicked on the permission checkbox")

    """Users actions"""
    def click_users_tab(self):
        self.get_users_tab().click()
        print("Clicked on the users tab")

    def click_new_user(self):
        self.get_new_user().click()
        print("Clicked on the new user button")

    def input_user_name(self):
        self.get_user_name().send_keys("Test name")
        print("Filled in the name field")

    def input_user_email(self):
        self.get_email().send_keys("alexqamiroshkin@gmail.com")
        print("Filled in the email field")

    def input_user_password(self):
        self.get_password().send_keys("qweQwe123#")
        print("Filled in the password")

    def input_user_password_confirmation(self):
        self.get_password_confirmation().send_keys("qweQwe123#")
        print("Filled in the password confirmation")

    def click_admin_role(self):
        self.get_admin_role().click()
        print("Clicked on the admin role checkbox")

    """Domain actions"""
    def click_domain(self):
        self.get_domain().click()
        print("Clicked on the domain tab")

    def click_new_domain(self):
        self.get_new_domain().click()
        print("Clicked on the new domain button")

    def input_domain_field(self):
        self.get_domain_field().send_keys("admin@example.com")
        print("Filled in the domain field")

    def click_select_domain(self):
        self.get_select_domain().click()
        print("Clicked on the select domain checkbox")

    def click_delete_domain(self):
        self.get_delete_domain().click()
        self.get_delete_domain_confirmation().click()
        print("Deleted the selected domain")

    # METHODS
    def roles_tab_test(self):
        with allure.step("roles tab test"):
            Logger.add_start_step(method="roles_tab_test")
            self.click_users()
            self.click_roles()
            self.click_new_role()
            self.input_genre_name()
            self.click_permission()
            self.click_save_changes_button()
            self.assert_word(self.get_success_notification(), "new item saved successfully")
            self.click_delete_item_button()
            self.click_delete_confirmation()
            Logger.add_end_step(url=self.driver.current_url, method="roles_tab_test")
            time.sleep(0.7)

    def users_tab_test(self):
        with allure.step("users tab test"):
            Logger.add_start_step(method="users_tab_test")
            self.click_users_tab()
            self.click_new_user()
            self.input_user_name()
            self.input_user_email()
            self.input_user_password()
            self.input_user_password_confirmation()
            self.click_admin_role()
            self.click_save_changes_button()
            self.assert_word(self.get_success_notification(), "new item saved successfully")
            self.click_delete_item_button()
            self.click_delete_confirmation()
            Logger.add_end_step(url=self.driver.current_url, method="users_tab_test")
            time.sleep(0.7)

    def domain_tab_test(self):
        with allure.step("domain tab test"):
            Logger.add_start_step(method="domain_tab_test")
            self.click_domain()
            self.click_new_domain()
            self.input_domain_field()
            self.click_save_changes_button()
            self.assert_word(self.get_success_notification(), "new item saved successfully")
            time.sleep(0.5)
            self.click_domain()
            self.click_select_domain()
            self.click_delete_domain()
            self.assert_word(self.get_deleted_notification(), "deleted successfully")
            Logger.add_end_step(url=self.driver.current_url, method="domain_tab_test")



