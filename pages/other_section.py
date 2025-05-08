from pages.users_section import UserSection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

from utilities.logger import Logger


class OtherSection(UserSection):
    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS
    """Agents locators"""
    OTHER = "//span[contains(text(), 'Other')]"
    AGENTS_TAB = "//a[contains(text(), 'Agents')]"
    NEW_AGENT = "//a[contains(text(), 'New Agent')]"
    COUNTRY = "(//input[@type='search'])[2]"
    RETAILER_CHECKBOX = "//div[@class='checkbox__control__indicator']"
    WEBSITE = "//input[@name='website']"

    """App stores locators"""
    APP_STORES = "//a[contains(text(), 'App stores')]"
    NEW_STORE = "//a[contains(text(), 'New Store')]"
    OWNER_DROPDOWN = "//div[@class='choices__item choices__item--selectable']"
    OWNER_SEARCH = "//input[@type='search']"
    OWNER_URL = "//input[@name='url']"

    """Brands locators"""
    BRANDS = "//a[contains(text(), 'Brands')]"
    NEW_BRAND = "//a[contains(text(), 'New Brand')]"
    BRAND_COUNTRY = "//div[@class='choices mb-0 flex-1']"
    BRAND_COUNTRY_SEARCH = "//input[@type='search']"

    """Countries locators"""
    COUNTRIES = "//a[contains(text(), 'Countries')]"
    NEW_COUNTRY = "//a[contains(text(), 'New Country')]"

    """Currencies locators"""
    CURRENCIES = "//a[contains(text(), 'Currencies')]"
    NEW_CURRENCIES = "//a[contains(text(), 'New Currency')]"
    SYMBOL = "//input[@name='symbol']"
    CURRENCIES_DROPDOWN = "//div[@class='choices mb-0 flex-1']"
    CURRENCIES_COUNTRY = "//input[@type='search']"

    """Measure locators"""
    MEASURE = "//a[contains(text(), 'Measure')]"
    NEW_MEASURE = "//a[contains(text(), 'New Measure')]"
    SHORT_NAME = "//input[@name='short_name']"

    """Websites locators"""
    WEBSITES = "//a[contains(text(), 'Websites')]"
    NEW_WEBSITE = "//a[contains(text(), 'New Website')]"
    WEBSITE_DOMAIN = "(//input[@type='text'])[4]"

    """Domains locators"""
    ALLOWED_DOMAIN = "//a[contains(text(), 'Allowed domains')]"
    NEW_ALLOWED_DOMAIN = "//a[contains(text(), 'New Domain')]"
    DOMAIN_ALLOWED_FIELD = "//input[@name='domain']"

    """Badges locators"""
    BADGES = "//a[contains(text(), 'Award badges')]"
    NEW_BADGE = "//a[contains(text(), 'New badge')]"

    """Tags locators"""
    TAG = "//a[contains(text(), 'Tags')]"
    NEW_TAG = "//a[contains(text(), 'New tag')]"

    """Deal tags locators"""
    DEAL_TAG = "//a[contains(text(), 'Deal Tags')]"

    # GETTERS
    """Agents getters"""
    def get_other(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.OTHER)))

    def get_agents_tab(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.AGENTS_TAB)))

    def get_new_agent(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_AGENT)))

    def get_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.COUNTRY)))

    def get_retailer_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.RETAILER_CHECKBOX)))

    def get_website(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.WEBSITE)))

    """App stores getters"""
    def get_app_stores(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.APP_STORES)))

    def get_new_store(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_STORE)))

    def get_owner_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.OWNER_DROPDOWN)))

    def get_owner_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.OWNER_SEARCH)))

    def get_owner_url(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.OWNER_URL)))

    """Brands getters"""
    def get_brands(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.BRANDS)))

    def get_new_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_BRAND)))

    def get_brand_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.BRAND_COUNTRY)))

    def get_brand_country_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.BRAND_COUNTRY_SEARCH)))

    """Countries getters"""
    def get_countries(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.COUNTRIES)))

    def get_new_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_COUNTRY)))

    """Currencies getters"""
    def get_currencies(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.CURRENCIES)))

    def get_new_currencies(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_CURRENCIES)))

    def get_symbol(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.SYMBOL)))

    def get_currencies_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.CURRENCIES_DROPDOWN)))

    def get_currencies_country_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.CURRENCIES_COUNTRY)))

    """Measure getters"""
    def get_measure(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.MEASURE)))

    def get_new_measure(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_MEASURE)))

    def get_short_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.SHORT_NAME)))

    """Websites getters"""
    def get_websites(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.WEBSITES)))

    def get_new_website(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_WEBSITE)))

    def get_website_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.WEBSITE_DOMAIN)))

    """Domains getters"""
    def get_allowed_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ALLOWED_DOMAIN)))

    def get_new_allowed_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_ALLOWED_DOMAIN)))

    def get_domain_allowed_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.DOMAIN_ALLOWED_FIELD)))

    """Badges getters"""
    def get_badges(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.BADGES)))

    def get_new_badge(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_BADGE)))

    """Tags getters"""
    def get_tag(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.TAG)))

    def get_new_tag(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_TAG)))

    """Deal tags getters"""
    def get_deal_tag(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.DEAL_TAG)))

    # ACTIONS
    """Agents actions"""
    def click_other(self):
        self.get_other().click()
        print("Clicked on the other section")

    def click_agents_tab(self):
        self.get_agents_tab().click()
        print("Clicked on the agents tab")

    def click_new_agent(self):
        self.get_new_agent().click()
        print("Clicked on the new agent button")

    def input_country(self):
        self.get_country().click()
        self.get_country().send_keys("a")
        self.get_country().send_keys(Keys.RETURN)
        print("Filled in country")

    def click_retailer_checkbox(self):
        self.get_retailer_checkbox().click()
        print("Clicked on the retailer checkbox")

    def click_website(self):
        self.get_website().click()
        print("Clicked on website")

    """App stores actions"""
    def click_app_stores(self):
        self.get_app_stores().click()
        print("Clicked on the app stores tab")

    def click_new_store(self):
        self.get_new_store().click()
        print("Clicked on the new store button")

    def click_owner_dropdown(self):
        self.get_owner_dropdown().click()
        self.get_owner_search().click()
        self.get_owner_search().send_keys("a")
        self.get_owner_search().send_keys(Keys.RETURN)
        print("Clicked on the owner dropdown")

    def input_owner_url(self):
        self.get_owner_url().send_keys("https://demoqa.com/")

    """Brands actions"""
    def click_brands(self):
        self.get_brands().click()
        print("Clicked on the brands tab")

    def click_new_brand(self):
        self.get_new_brand().click()
        print("Clicked on the new brand button")

    def click_brand_country(self):
        self.get_brand_country().click()
        self.get_brand_country_search().click()
        self.get_brand_country_search().send_keys("a")
        self.get_brand_country_search().send_keys(Keys.RETURN)
        print("Clicked on the country brand dropdown")

    """Countries actions"""
    def click_countries(self):
        self.get_countries().click()
        print("Clicked on the countries tab")

    def click_new_country(self):
        self.get_new_country().click()
        print("Clicked on the new country button")

    """Currencies actions"""
    def click_currencies(self):
        self.get_currencies().click()
        print("Clicked on the currencies tab")

    def click_new_currencies(self):
        self.get_new_currencies().click()
        print("Clicked on the new currencies tab")

    def input_symbol(self):
        self.get_symbol().send_keys("$")
        print("Filled in symbol field")

    def click_get_currencies_country_dropdown(self):
        self.get_currencies_dropdown().click()
        self.get_currencies_country_search().click()
        self.get_currencies_country_search().send_keys("a")
        self.get_currencies_country_search().send_keys(Keys.RETURN)
        print("Clicked on the currencies dropdown")

    """Measure actions"""
    def click_get_measure(self):
        self.get_measure().click()
        print("Clicked on the measure tab")

    def click_new_measure(self):
        self.get_new_measure().click()
        print("Clicked on the new measure button")

    def input_short_name(self):
        self.get_short_name().send_keys("Short")
        print("Filled in short name field")

    """Websites actions"""
    def click_websites(self):
        self.get_websites().click()
        print("Clicked on the websites tab")

    def click_new_website(self):
        self.get_new_website().click()
        print("Clicked on the new website button")

    def input_website_domain(self):
        self.get_website_domain().send_keys("example")
        print("Filled in domain field")

    """Domains actions"""
    def click_allowed_domain(self):
        self.get_allowed_domain().click()
        print("Clicked on the domains tab")

    def click_new_allowed_domain(self):
        self.get_new_allowed_domain().click()
        print("Clicked on the new domain tab")

    def input_domain_allowed_field(self):
        self.get_domain_allowed_field().send_keys("example")
        print("Filled in allowed domain field")

    """Badges actions"""
    def click_get_badges(self):
        self.get_badges().click()
        print("Clicked on the badges tab")

    def click_new_badge(self):
        self.get_new_badge().click()
        print("Clicked on the new badge button")

    """Tags actions"""
    def click_tag(self):
        self.get_tag().click()
        print("Clicked on the tags tab")

    def click_new_tag(self):
        self.get_new_tag().click()
        print("Clicked on the new tag button")

    """Deal tags actions"""
    def click_deal_tag(self):
        self.get_deal_tag().click()
        print("Clicked on the deal tags tab")

    # METHODS
    def other_tab_test(self):
        Logger.add_start_step(method="other_tab_test")
        self.click_other()
        self.click_agents_tab()
        self.click_new_agent()
        self.input_genre_name()
        self.input_country()
        self.click_website()
        self.click_retailer_checkbox()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        Logger.add_end_step(url=self.driver.current_url, method="other_tab_test")
        time.sleep(0.7)

    def app_stores_tab_test(self):
        Logger.add_start_step(method="app_stores_tab_test")
        self.click_app_stores()
        self.click_new_store()
        self.input_genre_name()
        self.click_owner_dropdown()
        self.input_owner_url()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        Logger.add_end_step(url=self.driver.current_url, method="app_stores_tab_test")
        time.sleep(0.7)

    def brands_tab_test(self):
        Logger.add_start_step(method="brands_tab_test")
        self.click_brands()
        self.click_new_brand()
        self.input_genre_name()
        self.click_brand_country()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        Logger.add_end_step(url=self.driver.current_url, method="brands_tab_test")
        time.sleep(0.7)

    def countries_tab_test(self):
        Logger.add_start_step(method="countries_tab_test")
        self.click_countries()
        self.click_new_country()
        self.input_genre_name()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        Logger.add_end_step(url=self.driver.current_url, method="countries_tab_test")
        time.sleep(0.7)

    def currencies_tab_test(self):
        Logger.add_start_step(method="currencies_tab_test")
        self.click_currencies()
        self.click_new_currencies()
        self.input_genre_name()
        self.input_symbol()
        self.click_get_currencies_country_dropdown()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        Logger.add_end_step(url=self.driver.current_url, method="currencies_tab_test")
        time.sleep(0.7)

    def measure_tab_test(self):
        Logger.add_start_step(method="measure_tab_test")
        self.click_get_measure()
        self.click_new_measure()
        self.input_genre_name()
        self.input_short_name()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        Logger.add_end_step(url=self.driver.current_url, method="measure_tab_test")
        time.sleep(0.7)

    def websites_tab_test(self):
        Logger.add_start_step(method="websites_tab_test")
        self.click_websites()
        self.click_new_website()
        self.input_genre_name()
        self.input_website_domain()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        Logger.add_end_step(url=self.driver.current_url, method="websites_tab_test")
        time.sleep(0.7)

    def domains_tab_test(self):
        Logger.add_start_step(method="domains_tab_test")
        self.click_allowed_domain()
        self.click_new_allowed_domain()
        self.input_domain_allowed_field()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "New item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        Logger.add_end_step(url=self.driver.current_url, method="domains_tab_test")
        time.sleep(0.7)

    def badges_tab_test(self):
        Logger.add_start_step(method="badges_tab_test")
        self.click_get_badges()
        self.click_new_badge()
        self.input_genre_name()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        Logger.add_end_step(url=self.driver.current_url, method="badges_tab_test")
        time.sleep(0.7)

    def tags_tab_test(self):
        Logger.add_start_step(method="tags_tab_test")
        self.click_tag()
        self.click_new_tag()
        self.input_genre_name()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        Logger.add_end_step(url=self.driver.current_url, method="tags_tab_test")
        time.sleep(0.7)

    def deal_tags_test(self):
        Logger.add_start_step(method="deal_tags_test")
        self.click_deal_tag()
        self.click_new_tag()
        self.input_genre_name()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        Logger.add_end_step(url=self.driver.current_url, method="deal_tags_test")



