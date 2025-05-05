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
    os = "//span[contains(text(), 'OS')]"
    license = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[16]"
    new_license = "//a[contains(text(), 'New License')]"
    os_tab = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[17]"
    new_os = "//a[contains(text(), 'New OS')]"
    os_url = "(//input[@class='border w-full rounded-md px-4 py-2'])[2]"
    brand_os_dropdown = "(//div[@class='choices__item choices__item--selectable'])[1]"
    brand_os_search = "(//input[@type='search'])[1]"
    license_dropdown = "(//div[@class='choices__item choices__item--selectable'])[2]"
    license_search = "(//input[@type='search'])[2]"
    releases_tab = "//a[contains(text(), 'Releases')]"
    add_button = "//a[contains(text(), 'Add')]"
    version = "//input[@name='releases[0][version]']"
    date = "//input[@type='date']"


    # GETTERS
    def get_os(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.os)))

    def get_license(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.license)))

    def get_new_license(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_license)))

    def get_os_tab(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.os_tab)))

    def get_new_os(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_os)))

    def get_os_url(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.os_url)))

    def get_brand_os_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_os_dropdown)))

    def get_brand_os_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_os_search)))

    def get_license_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.license_dropdown)))

    def get_license_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.license_search)))

    def get_releases_tab(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.releases_tab)))

    def get_add_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_button)))

    def get_version(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.version)))

    def get_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.date)))

    # ACTIONS
    def click_os(self):
        self.get_os().click()
        print("Clicked on the os section")

    def click_license(self):
        self.get_license().click()
        print("Clicked on the license tab")

    def click_new_license(self):
        self.get_new_license().click()
        print("Clicked on the new license button")

    def click_os_tab(self):
        self.get_os_tab().click()
        print("Clicked on the os tab")

    def click_new_os(self):
        self.get_new_os().click()
        print("Clicked on the new os button")

    def input_os_url(self):
        self.get_os_url().send_keys("https://demoqa.com/")
        print("Filled in os url")

    def click_brand_os_dropdown(self):
        self.get_brand_os_dropdown().click()
        self.get_brand_os_search().click()
        self.get_brand_os_search().send_keys("a")
        self.get_brand_os_search().send_keys(Keys. RETURN)
        print("Clicked brand dropdown")

    def click_license_dropdown(self):
        self.get_license_dropdown().click()
        self.get_license_search().click()
        self.get_license_search().send_keys(Keys. DOWN)
        self.get_license_search().send_keys(Keys. RETURN)
        print("Clicked license dropdown")

    def click_releases_tab(self):
        self.get_releases_tab().click()
        self.get_add_button().click()
        print("Clicked on the releases tab")

    def input_version(self):
        self.get_version().send_keys("Test version")
        print("Filled in version")

    def click_date(self):
        self.get_date().click()
        self.get_product_date().send_keys("12")
        self.get_product_date().send_keys("4")
        self.get_product_date().send_keys(Keys.RIGHT)
        self.get_product_date().send_keys("2025")
        print("Filled in date")

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


