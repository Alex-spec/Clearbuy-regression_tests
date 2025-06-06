import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.base_methods import BasePage
from pages.products_section import ProductsSectionSteps
from utilities.logger import Logger

class OsSectionsLocators:

    # OS and Licenses locators

    OS = (By.XPATH, "//span[contains(text(), 'OS')]")
    LICENSE = (By.XPATH, "//a[text()='Licenses']")
    NEW_LICENSE = (By.XPATH, "//a[contains(text(), 'New License')]")
    NEW_LICENSE_NAME = (By.XPATH, "//input[@name='name']")
    OS_TAB = (By.XPATH, "//a[text()='OS']")
    NEW_OS = (By.XPATH, "//a[contains(text(), 'New OS')]")
    OS_URL = (By.XPATH, "(//input[@class='border w-full rounded-md px-4 py-2'])[2]")
    BRAND_OS_DROPDOWN = (By.XPATH, "(//div[@class='choices__item choices__item--selectable'])[1]")
    BRAND_OS_SEARCH = (By.XPATH, "(//input[@type='search'])[1]")
    LICENSE_DROPDOWN = (By.XPATH, "(//div[@class='choices__item choices__item--selectable'])[2]")
    LICENSE_SEARCH = (By.XPATH, "(//input[@type='search'])[2]")
    RELEASES_TAB = (By.XPATH, "//a[contains(text(), 'Releases')]")
    ADD_BUTTON = (By.XPATH, "//a[contains(text(), 'Add')]")
    VERSION = (By.XPATH, "//input[@name='releases[0][version]']")
    DATE = (By.XPATH, "//input[@type='date']")

class OsSectionGetters(BasePage):

    # OS getters

    def get_os(self):
        return self.wait_for_clickable(OsSectionsLocators.OS)

    def get_license(self):
        return self.wait_for_clickable(OsSectionsLocators.LICENSE)

    def get_new_license(self):
        return self.wait_for_clickable(OsSectionsLocators.NEW_LICENSE)

    def get_os_tab(self):
        return self.wait_for_clickable(OsSectionsLocators.OS_TAB)

    def get_new_os(self):
        return self.wait_for_clickable(OsSectionsLocators.NEW_OS)

    def get_os_url(self):
        return self.wait_for_clickable(OsSectionsLocators.OS_URL)

    def get_brand_os_dropdown(self):
        return self.wait_for_clickable(OsSectionsLocators.BRAND_OS_DROPDOWN)

    def get_brand_os_search(self):
        return self.wait_for_clickable(OsSectionsLocators.BRAND_OS_SEARCH)

    def get_license_dropdown(self):
        return self.wait_for_clickable(OsSectionsLocators.LICENSE_DROPDOWN)

    def get_license_search(self):
        return self.wait_for_clickable(OsSectionsLocators.LICENSE_SEARCH)

    def get_releases_tab(self):
        return self.wait_for_clickable(OsSectionsLocators.RELEASES_TAB)

    def get_add_button(self):
        return self.wait_for_clickable(OsSectionsLocators.ADD_BUTTON)

    def get_version(self):
        return self.wait_for_clickable(OsSectionsLocators.VERSION)

    def get_date(self):
        return self.wait_for_clickable(OsSectionsLocators.DATE)

class OsSectionActions(OsSectionGetters):

    def click_os(self):
        self.get_os().click()
        print("Clicked on the OS section")

    def click_license(self):
        self.get_license().click()
        print("Clicked on the License tab")

    def click_new_license(self):
        self.get_new_license().click()
        print("Clicked on the New License button")

    def click_os_tab(self):
        self.get_os_tab().click()
        print("Clicked on the OS tab")

    def click_new_os(self):
        self.get_new_os().click()
        print("Clicked on the New OS button")

    def input_os_url(self):
        self.get_os_url().send_keys("https://demoqa.com/")
        print("Filled in OS URL")

    def click_brand_os_dropdown(self):
        self.get_brand_os_dropdown().click()
        self.get_brand_os_search().click()
        self.get_brand_os_search().send_keys("a")
        self.get_brand_os_search().send_keys(Keys.RETURN)
        print("Clicked Brand OS dropdown and searched")

    def click_license_dropdown(self):
        self.get_license_dropdown().click()
        self.get_license_search().click()
        self.get_license_search().send_keys(Keys.DOWN)
        self.get_license_search().send_keys(Keys.RETURN)
        print("Clicked License dropdown and selected")

    def click_releases_tab(self):
        self.get_releases_tab().click()
        self.get_add_button().click()
        print("Clicked on the Releases tab and Add button")

    def input_version(self):
        self.get_version().send_keys("Test version")
        print("Filled in Version")

    def input_new_license_name(self):
        self.input_text(OsSectionsLocators.NEW_LICENSE_NAME, "Test name")

    def click_date(self):
        self.get_date().click()
        self.get_date().send_keys("12")
        self.get_date().send_keys("4")
        self.get_date().send_keys(Keys.RIGHT)
        self.get_date().send_keys("2025")
        print("Filled in Date")

class OsSectionSteps(OsSectionActions, ProductsSectionSteps):
    def licenses_tab_test(self):
        with allure.step("licenses tab test"):
            Logger.add_start_step(method="licenses_tab_test")
            self.click_os()
            self.click_license()
            self.click_new_license()
            self.input_new_license_name()
            self.click_save_changes_button()
            self.click_delete_item_button()
            self.click_delete_confirmation()
            Logger.add_end_step(url=self.driver.current_url, method="licenses_tab_test")
            time.sleep(0.7)

    def os_tab_test(self):
        with allure.step("os tab test"):
            Logger.add_start_step(method="os_tab_test")
            self.click_os_tab()
            self.click_new_os()
            self.input_new_license_name()
            self.input_os_url()
            self.click_brand_os_dropdown()
            self.click_license_dropdown()
            self.click_releases_tab()
            self.input_version()
            self.click_date()
            self.click_save_changes_button()
            self.assert_word(self.get_success_notification(), "saved successfully")
            self.click_delete_item_button()
            self.click_delete_confirmation()
            Logger.add_end_step(url=self.driver.current_url, method="os_tab_test")


