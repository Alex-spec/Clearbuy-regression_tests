from pages.films_section import FilmSection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

class OsSection(FilmSection):
    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS
    OS = "//span[contains(text(), 'OS')]"
    LICENSE = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[16]"
    NEW_LICENSE = "//a[contains(text(), 'New License')]"
    OS_TAB = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[17]"
    NEW_OS = "//a[contains(text(), 'New OS')]"
    OS_URL = "(//input[@class='border w-full rounded-md px-4 py-2'])[2]"
    BRAND_OS_DROPDOWN = "(//div[@class='choices__item choices__item--selectable'])[1]"
    BRAND_OS_SEARCH = "(//input[@type='search'])[1]"
    LICENSE_DROPDOWN = "(//div[@class='choices__item choices__item--selectable'])[2]"
    LICENSE_SEARCH = "(//input[@type='search'])[2]"
    RELEASES_TAB = "//a[contains(text(), 'Releases')]"
    ADD_BUTTON = "//a[contains(text(), 'Add')]"
    VERSION = "//input[@name='releases[0][version]']"
    DATE = "//input[@type='date']"

    # GETTERS
    def get_os(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.OS)))

    def get_license(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.LICENSE)))

    def get_new_license(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_LICENSE)))

    def get_os_tab(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.OS_TAB)))

    def get_new_os(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_OS)))

    def get_os_url(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.OS_URL)))

    def get_brand_os_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.BRAND_OS_DROPDOWN)))

    def get_brand_os_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.BRAND_OS_SEARCH)))

    def get_license_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.LICENSE_DROPDOWN)))

    def get_license_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.LICENSE_SEARCH)))

    def get_releases_tab(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.RELEASES_TAB)))

    def get_add_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ADD_BUTTON)))

    def get_version(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.VERSION)))

    def get_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.DATE)))

    # ACTIONS
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

    def click_date(self):
        self.get_date().click()
        self.get_date().send_keys("12")
        self.get_date().send_keys("4")
        self.get_date().send_keys(Keys.RIGHT)
        self.get_date().send_keys("2025")
        print("Filled in Date")

    # METHODS
    def licenses_tab_test(self):
        self.click_os()
        self.click_license()
        self.click_new_license()
        self.input_genre_name()
        self.click_save_changes_button()
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def os_tab_test(self):
        self.click_os_tab()
        self.click_new_os()
        self.input_genre_name()
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


