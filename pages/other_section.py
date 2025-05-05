from pages.users_section import UserSection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

class OtherSection(UserSection):
    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS
    """Agents locators"""
    other = "//span[contains(text(), 'Other')]"
    agents_tab = "//a[contains(text(), 'Agents')]"
    new_agent = "//a[contains(text(), 'New Agent')]"
    country = "(//input[@type='search'])[2]"
    retailer_checkbox = "//div[@class='checkbox__control__indicator']"
    website = "//input[@name='website']"

    """App stores locators"""
    app_stores = "//a[contains(text(), 'App stores')]"
    new_store = "//a[contains(text(), 'New Store')]"
    owner_dropdown = "//div[@class='choices__item choices__item--selectable']"
    owner_search = "//input[@type='search']"
    owner_url = "//input[@name='url']"

    """Brands locators"""
    brands = "//a[contains(text(), 'Brands')]"
    new_brand = "//a[contains(text(), 'New Brand')]"
    brand_country = "//div[@class='choices mb-0 flex-1']"
    brand_country_search = "//input[@type='search']"

    """Countries locators"""
    countries = "//a[contains(text(), 'Countries')]"
    new_country = "//a[contains(text(), 'New Country')]"

    """Currencies locators"""
    currencies = "//a[contains(text(), 'Currencies')]"
    new_currencies = "//a[contains(text(), 'New Currency')]"
    symbol = "//input[@name='symbol']"
    currencies_dropdown = "//div[@class='choices mb-0 flex-1']"
    currencies_country = "//input[@type='search']"

    """Measure locators"""
    measure = "//a[contains(text(), 'Measure')]"
    new_measure = "//a[contains(text(), 'New Measure')]"
    short_name = "//input[@name='short_name']"

    """Websites locators"""
    websites = "//a[contains(text(), 'Websites')]"
    new_website = "//a[contains(text(), 'New Website')]"
    website_domain = "(//input[@type='text'])[4]"

    """Domains locators"""
    allowed_domain = "//a[contains(text(), 'Allowed domains')]"
    new_allowed_domain = "//a[contains(text(), 'New Domain')]"
    domain_allowed_field = "//input[@name='domain']"

    """Badges locators"""
    badges = "//a[contains(text(), 'Award badges')]"
    new_badge = "//a[contains(text(), 'New badge')]"

    """Tags locators"""
    tag = "//a[contains(text(), 'Tags')]"
    new_tag = "//a[contains(text(), 'New tag')]"

    """Deal tags locators"""
    deal_tag = "//a[contains(text(), 'Deal Tags')]"

    # GETTERS
    """Agents getters"""
    def get_other(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.other)))

    def get_agents_tab(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.agents_tab)))

    def get_new_agent(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_agent)))

    def get_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.country)))

    def get_retailer_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.retailer_checkbox)))

    def get_website(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.website)))

    """App stores getters"""
    def get_app_stores(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.app_stores)))

    def get_new_store(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_store)))

    def get_owner_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.owner_dropdown)))

    def get_owner_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.owner_search)))

    def get_owner_url(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.owner_url)))

    """Brands getters"""
    def get_brands(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brands)))

    def get_new_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_brand)))

    def get_brand_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_country)))

    def get_brand_country_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_country_search)))

    """Countries getters"""
    def get_countries(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.countries)))

    def get_new_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_country)))

    """Currencies getters"""
    def get_currencies(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.currencies)))

    def get_new_currencies(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_currencies)))

    def get_symbol(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.symbol)))

    def get_currencies_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.currencies_dropdown)))

    def get_currencies_country_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.currencies_country)))

    """Measure getters"""
    def get_measure(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.measure)))

    def get_new_measure(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_measure)))

    def get_short_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.short_name)))

    """Websites getters"""
    def get_websites(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.websites)))

    def get_new_website(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_website)))

    def get_website_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.website_domain)))

    """Domains getters"""
    def get_allowed_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.allowed_domain)))

    def get_new_allowed_domain(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_allowed_domain)))

    def get_domain_allowed_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.domain_allowed_field)))

    """Badges getters"""
    def get_badges(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.badges)))

    def get_new_badge(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_badge)))

    """Tags getters"""
    def get_tag(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.tag)))

    def get_new_tag(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_tag)))

    """Deal tags getters"""
    def get_deal_tag(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.deal_tag)))

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
        self.get_owner_search().send_keys(Keys. RETURN)
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
        time.sleep(0.7)

    def app_stores_tab_test(self):
        self.click_app_stores()
        self.click_new_store()
        self.input_genre_name()
        self.click_owner_dropdown()
        self.input_owner_url()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def brands_tab_test(self):
        self.click_brands()
        self.click_new_brand()
        self.input_genre_name()
        self.click_brand_country()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def countries_tab_test(self):
        self.click_countries()
        self.click_new_country()
        self.input_genre_name()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def currencies_tab_test(self):
        self.click_currencies()
        self.click_new_currencies()
        self.input_genre_name()
        self.input_symbol()
        self.click_get_currencies_country_dropdown()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def measure_tab_test(self):
        self.click_get_measure()
        self.click_new_measure()
        self.input_genre_name()
        self.input_short_name()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def websites_tab_test(self):
        self.click_websites()
        self.click_new_website()
        self.input_genre_name()
        self.input_website_domain()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def domains_tab_test(self):
        self.click_allowed_domain()
        self.click_new_allowed_domain()
        self.input_domain_allowed_field()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "New item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def badges_tab_test(self):
        self.click_get_badges()
        self.click_new_badge()
        self.input_genre_name()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def tags_tab_test(self):
        self.click_tag()
        self.click_new_tag()
        self.input_genre_name()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def deal_tags_test(self):
        self.click_deal_tag()
        self.click_new_tag()
        self.input_genre_name()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()



