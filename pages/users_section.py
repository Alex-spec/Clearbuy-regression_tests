from pages.os_section import OsSection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class UserSection(OsSection):
    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS
    """Roles locators"""
    users = "//span[contains(text(), 'Users')]"
    roles = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[18]"
    new_role = "//a[contains(text(), 'New Role')]"
    permission = "(//div[@class='mr-1 checkbox__control'])[1]"

    """Users locators"""
    users_tab = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[19]"
    new_user = "//a[contains(text(), 'New User')]"
    user_name = "//input[@name='name']"
    email = "//input[@name='email']"
    password = "//input[@name='password']"
    password_confirmation = "//input[@name='password_confirmation']"
    admin_role = "(//div[@class='checkbox__control__indicator'])[1]"

    """Domains locators"""
    domain = "//a[contains(text(), 'Allowed auth domains')]"
    new_domain = "//a[contains(text(), 'Domain')]"
    domain_field ="//input[@name='domain']"
    select_domain = "(//input[@class='selectAllCheckable'])[1]"
    delete_domain = "//a[contains(text(), 'Delete Selected')]"
    delete_domain_confirmation = "//a[normalize-space(text()) = 'Delete']"

    # GETTERS
    """Roles getters"""
    def get_users(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.users)))

    def get_roles(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.roles)))

    def get_new_role(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_role)))

    def get_permission(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.permission)))

    """Users getters"""
    def get_users_tab(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.users_tab)))

    def get_new_user(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_user)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_password_confirmation(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_confirmation)))

    def get_admin_role(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.admin_role)))

    """Domains getters"""
    def get_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.domain)))

    def get_new_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_domain)))

    def get_domain_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.domain_field)))

    def get_select_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_domain)))

    def get_delete_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_domain)))

    def get_delete_domain_confirmation(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_domain_confirmation)))

    # ACTIONS
    """Roles actions"""
    def click_users(self):
        self.get_users().click()
        print("Clicked on the users sections")

    def click_roles(self):
        self.get_roles().click()
        print("Clicked on the roles tab")

    def click_new_role(self):
        self.get_new_role().click()
        print("Clicked on the new role button")

    def click_permission(self):
        self.get_permission().click()
        print("Clicked on the permission")

    """Users actions"""
    def click_users_tab(self):
        self.get_users_tab().click()
        print("Clicked on the users tab")

    def click_new_user(self):
        self.get_new_user().click()
        print("Clicked on the new user button")

    def input_user_name(self):
        self.get_user_name().send_keys("Test name")
        print("Filled in name field")

    def input_user_email(self):
        self.get_email().send_keys("alexqamiroshkin@gmail.com")
        print("Filled in email field")

    def input_user_password(self):
        self.get_password().send_keys("qweQwe123#")
        print("Filled in password")

    def input_user_password_confirmation(self):
        self.get_password_confirmation().send_keys("qweQwe123#")
        print("Filled in password confirmation")

    def click_admin_role(self):
        self.get_admin_role().click()
        print("Clicked on the admin role")

    """Domain actions"""
    def click_domain(self):
        self.get_domain().click()
        print("Clicked on the domain tab")

    def click_new_domain(self):
        self.get_new_domain().click()
        print("Clicked on the new domain button")

    def input_domain_field(self):
        self.get_domain_field().send_keys("admin@example.com")
        print("Filled in domain field")

    def click_select_domain(self):
        self.get_select_domain().click()
        print("Clicked on the select option")

    def click_delete_domain(self):
        self.get_delete_domain().click()
        self.get_delete_domain_confirmation().click()
        print("Clicked on the delete option")

    # METHODS
    def roles_tab_test(self):
        self.click_users()
        self.click_roles()
        self.click_new_role()
        self.input_genre_name()
        self.click_permission()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def users_tab_test(self):
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
        time.sleep(0.7)

    def domain_tab_test(self):
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
        time.sleep(5)


