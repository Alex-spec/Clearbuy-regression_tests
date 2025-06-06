import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.base_methods import BasePage
from pages.products_section import ProductsSectionActions
from utilities.logger import Logger

class AppsSectionLocators:
    APPS = (By.XPATH, "//a[contains(text(), 'Apps')]")
    NEW_APP = (By.XPATH, "//a[contains(text(), 'New App')]")
    APP_NAME = (By.XPATH, "//input[@name='name']")
    RELATIONS_TAB = (By.XPATH, "(//a[@class='block px-6 py-2'])[2]")
    APPS_DROPDOWN = (By.XPATH, "(//div[@data-type='select-one'])[2]")
    APPS_SEARCH = (By.XPATH, "(//input[@type='search'])[2]")

class AppsSectionGetters(BasePage):
    def get_apps(self):
        return self.wait_for_clickable(AppsSectionLocators.APPS)

    def get_new_app(self):
        return self.wait_for_clickable(AppsSectionLocators.NEW_APP)

    def get_relations_tab(self):
        return self.wait_for_clickable(AppsSectionLocators.RELATIONS_TAB)

    def get_apps_dropdown(self):
        return self.wait_for_clickable(AppsSectionLocators.APPS_DROPDOWN)

    def get_apps_search(self):
        return self.wait_for_clickable(AppsSectionLocators.APPS_SEARCH)

class AppsSectionActions(AppsSectionGetters):

    def click_apps(self):
        self.get_apps().click()
        print("Clicked on the apps section")

    def click_new_app(self):
        self.get_new_app().click()
        print("Clicked on the new app button")

    def input_app_name(self):
        self.input_text(AppsSectionLocators.APP_NAME, "Test name")

    def click_relations_tab(self):
        self.get_relations_tab().click()
        print("Clicked on the relations tab")

    def click_apps_dropdown(self):
        self.get_apps_dropdown().click()
        self.get_apps_search().click()
        self.get_apps_search().send_keys("a")
        self.get_apps_search().send_keys(Keys.RETURN)
        print("Clicked on the brand dropdown")

class AppsSectionSteps(AppsSectionActions, ProductsSectionActions):
    def apps_tab_test(self):
        with allure.step("apps tab test"):
            Logger.add_start_step(method="apps_tab_test")
            self.driver.execute_script("document.querySelector('.phpdebugbar').style.display = 'none';")
            self.click_apps()
            self.click_new_app()
            self.input_app_name()
            self.click_relations_tab()
            self.click_apps_dropdown()
            self.click_save_changes_button()
            self.assert_word(self.get_success_notification(), "saved successfully")
            self.click_delete_item_button()
            self.click_delete_confirmation()
            Logger.add_end_step(url=self.driver.current_url, method="apps_tab_test")
