from pages.other_section import OtherSection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

class AppsSection(OtherSection):
    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS
    apps = "//a[contains(text(), 'Apps')]"
    new_app = "//a[contains(text(), 'New App')]"
    relations_tab = "(//a[@class='block px-6 py-2'])[2]"
    apps_dropdown = "(//div[@data-type='select-one'])[2]"
    apps_search = "(//input[@type='search'])[2]"

    # GETTERS
    def get_apps(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apps)))

    def get_new_app(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_app)))

    def get_relations_tab(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.relations_tab)))

    def get_apps_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apps_dropdown)))

    def get_apps_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apps_search)))

    # ACTIONS
    def click_apps(self):
        self.get_apps().click()
        print("Clicked on the apps section")

    def click_new_app(self):
        self.get_new_app().click()
        print("Clicked on the new app button")

    def click_relations_tab(self):
        self.get_relations_tab().click()
        print("Clicked on the relations tab")

    def click_apps_dropdown(self):
        self.get_apps_dropdown().click()
        self.get_apps_search().click()
        self.get_apps_search().send_keys("a")
        self.get_apps_search().send_keys(Keys.RETURN)
        print("Clicked on the brand dropdown")

    # METHODS
    def apps_tab_test(self):
        self.click_apps()
        self.click_new_app()
        self.input_genre_name()
        self.click_relations_tab()
        self.click_apps_dropdown()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(5)