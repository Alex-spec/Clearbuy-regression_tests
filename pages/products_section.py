from base.base_methods import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS
    """Attributes group locators"""
    attribute_groups = "(//ul[@class='mb-5 text-sm bg-primary bg-opacity-10'])[1]/li[1]"
    new_attribute_button = "//a[@class='font-semibold text-white font-grotesk bg-primary btn-shadow hover:bg-green-400 hover:shadow-none py-1 px-5 rounded']"
    name_attribute_field = "//input[@type='text']"
    sort_order = "//input[@type='number']"
    attribute_slider = "//span[@class='slider']"
    save_changes_button = "//a[contains(text(), 'Save changes')]"
    success_notification = "//div[@x-data='notification(0)']"
    delete_item_button ="//a[contains(text(), 'Delete item')]"
    delete_confirmation = "/html/body/div[3]/div/div/div/a[2]"
    deleted_notification = "//div[contains(text(), 'deleted successfully')]"

    """Attributes locators"""
    attributes = "(//ul[@class='mb-5 text-sm bg-primary bg-opacity-10'])[1]/li[2]"
    name_field = "//input[@name='name']"
    type_dropdown = "(//div[@role='combobox'])[2]"
    numeric_option = "//option[contains(text(), 'numeric')]"
    kind_checkbox = "(//div[@class='radio__control__indicator'])[1]"
    group_dropdown = "(//div[@role='combobox'])[3]"

    """Ratings locators"""
    ratings = "(//ul[@class='mb-5 text-sm bg-primary bg-opacity-10'])[1]/li[3]"
    ratings_slider = "//span[@class='slider']"
    speakers_checkbox = "(//div[@class='radio__control__indicator'])[1]"

    """Categories locators"""
    categories = "(//ul[@class='mb-5 text-sm bg-primary bg-opacity-10'])[1]/li[4]"
    commission_field = "//input[@name='commission_percent']"
    headphones_radiobutton = "(//div[@class='radio__control__indicator'])[1]"

    """Products locators"""
    products = "(//ul[@class='mb-5 text-sm bg-primary bg-opacity-10'])[1]/li[5]"
    category_dropdown = "(//div[@class='choices mb-0 flex-1'])[3]"
    category_option = "//div[@id='choices--category-item-choice-2']"
    brand_dropdown = "(//div[@class='choices mb-0 flex-1'])[3]"
    brand_search = "(//input[@class='choices__input choices__input--cloned'])[4]"
    retail_field = "//input[@name='price_msrp']"
    retail_select_dropdown = "(//div[@class='choices mb-0 flex-1'])[5]"
    select_search = "(//input[@class='choices__input choices__input--cloned'])[5]"
    product_date = "//input[@type='date']"
    product_save_changes_button = "//button[contains(text(), 'Save changes')]"
    delete_product_button = "//a[contains(text(), 'Delete product')]"
    delete_product_confirmation = "/html/body/div[1]/div[3]/div/div/div/a[2]"
    product_deleted_notification = "//div[contains(text(), 'Deleted successfully')]"

    """Deals locators"""
    deals = "(//ul[@class='mb-5 text-sm bg-primary bg-opacity-10'])[1]/li[6]"
    deal_price = "//input[@name='price']"
    deal_category = "(//div[@class='choices__item choices__item--selectable'])[2]"
    deal_category_search = "(//input[@type='search'])[2]"
    deal_url = "(//input[@name='url'])"
    deal_image = "//div[@class='flex']"
    image_option = "(//label[@x-data='{ isChecked: false }'])[1]"
    image_option_confirm = "//a[contains(text(), 'Confirm')]"

    """FAQ locators"""
    faq = "(//ul[@class='mb-5 text-sm bg-primary bg-opacity-10'])[1]/li[7]"
    faq_question = "//input[@name='question']"
    faq_answer = "//body[@id='tinymce']"

    """FAQ groups locators"""
    faq_groups = "(//ul[@class='mb-5 text-sm bg-primary bg-opacity-10'])[1]/li[8]"
    faq_groups_name = "//input[@name='name']"

    """Model families locators"""
    model = "(//ul[@class='mb-5 text-sm bg-primary bg-opacity-10'])[1]/li[9]"

    # GETTERS
    """Attribute groups getters"""

    def get_attribute_groups(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.attribute_groups)))

    def get_new_attribute_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_attribute_button)))

    def get_name_attribute_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_attribute_field)))

    def get_sort_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_order)))

    def get_attribute_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.attribute_slider)))

    def get_save_changes_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.save_changes_button)))

    def get_success_notification(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.success_notification)))

    def get_delete_item_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_item_button)))

    def get_delete_confirmation(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_confirmation)))

    def get_deleted_notification(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.deleted_notification)))

    """Attributes getters"""
    def get_attributes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.attributes)))

    def get_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_field)))

    def get_type_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.type_dropdown)))

    def get_numeric_option(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.numeric_option)))

    def get_kind_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.kind_checkbox)))

    def get_group_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.group_dropdown)))

    """Ratings getters"""
    def get_ratings(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ratings)))

    def get_ratings_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ratings_slider)))

    def get_speakers_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.speakers_checkbox)))

    """Categories getters"""
    def get_categories(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.categories)))

    def get_commission_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.commission_field)))

    def get_headphones_radiobutton(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.headphones_radiobutton)))

    """Products getters"""
    def get_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.products)))

    def get_category_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_dropdown)))

    def get_category_option(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_option)))

    def get_brand_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_dropdown)))

    def get_brand_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_search)))

    def get_retail_select_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.retail_select_dropdown)))

    def get_retail_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.retail_field)))

    def get_select_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_search)))

    def get_product_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_date)))

    def get_product_save_changes_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_save_changes_button)))

    def get_delete_product_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_product_button)))

    def get_delete_product_confirmation(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_product_confirmation)))

    def get_product_deleted_notification(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_deleted_notification)))

    """Deals getters"""
    def get_deals(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.deals)))

    def get_deal_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.deal_price)))

    def get_deal_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.deal_category)))

    def get_deal_category_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.deal_category_search)))

    def get_deal_url(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.deal_url)))

    def get_deal_image(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.deal_image)))

    def get_image_option(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.image_option)))

    def get_image_option_confirm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.image_option_confirm)))

    """Faq getters"""
    def get_faq(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.faq)))

    def get_faq_question(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.faq_question)))

    def get_faq_answer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.faq_answer)))

    """Faq groups getters"""
    def get_faq_groups(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.faq_groups)))

    def get_faq_groups_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.faq_groups_name)))

    """Model families getters"""
    def get_model(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.model)))

    # ACTIONS
    """Attribute groups actions"""
    def click_attribute_groups(self):
        self.get_attribute_groups().click()
        print("Clicked on the 'Attribute Groups' tab")

    def click_new_attribute_button(self):
        self.get_new_attribute_button().click()
        print("Clicked on the 'New Attribute' button")

    def input_name_attribute_field(self, text):
        self.get_name_attribute_field().send_keys(text)
        print("Entered test text into the name attribute field")

    def click_input_sort_order(self):
        self.get_sort_order().click()

    def input_sort_order(self, key):
        self.get_sort_order().send_keys(key)
        print("Filled in the 'Sort Order' field")

    def click_attribute_slider(self):
        self.get_attribute_slider().click()
        print("Clicked on the attribute slider")

    def click_save_changes_button(self):
        self.get_save_changes_button().click()
        print("Clicked the 'Save Changes' button")

    def click_delete_item_button(self):
        self.get_delete_item_button().click()
        print("Clicked the 'Delete Item' button")

    def click_attributes(self):
        self.get_attributes().click()
        print("Clicked on the 'Attributes' tab")

    """Attributes actions"""
    def click_delete_confirmation(self):
        self.get_delete_confirmation().click()
        print("Confirmed deletion")

    def input_name_field(self, text):
        self.get_name_field().send_keys(text)
        print("Filled in the 'Name' field")

    def click_type_dropdown(self):
        self.get_type_dropdown().click()
        self.get_type_dropdown().send_keys(Keys.DOWN)
        self.get_type_dropdown().send_keys(Keys.DOWN)
        self.get_type_dropdown().send_keys(Keys.RETURN)
        print("Clicked the 'Type' dropdown and selected an option")

    def click_kind_checkbox(self):
        self.get_kind_checkbox().click()
        print("Clicked on the kind checkbox")

    def click_group_dropdown(self):
        self.get_group_dropdown().click()
        self.get_group_dropdown().send_keys(Keys.DOWN)
        self.get_group_dropdown().send_keys(Keys.DOWN)
        self.get_group_dropdown().send_keys(Keys.RETURN)
        print("Clicked the 'Group' dropdown and selected an option")

    """Ratings actions"""
    def click_ratings(self):
        self.get_ratings().click()
        print("Clicked on the 'Ratings' tab")

    def click_ratings_slider(self):
        self.get_ratings_slider().click()
        print("Clicked on the ratings slider")

    def click_speakers_checkbox(self):
        self.get_speakers_checkbox().click()
        print("Clicked on the 'Speakers' radiobutton")

    """Categories actions"""
    def click_categories(self):
        self.get_categories().click()
        print("Clicked on the 'Categories' tab")

    def input_commission_field(self):
        self.get_commission_field().send_keys("15")
        print("Filled in the 'Commission' field")

    def click_headphones_radiobutton(self):
        self.get_headphones_radiobutton().click()
        print("Clicked on the 'Headphones' radiobutton")

    """Products actions"""
    def click_category_dropdown(self):
        self.get_category_dropdown().click()
        print("Clicked on the 'Category' dropdown")

    def click_get_products(self):
        self.get_products().click()
        print("Clicked on the 'Products' tab")

    def click_category_option(self):
        self.get_category_option().click()
        print("Clicked on a category option")

    def click_brand_dropdown(self):
        self.get_brand_dropdown().click()
        print("Clicked on the 'Brand' dropdown")

    def click_brand_search(self):
        self.get_brand_search().click()
        self.get_brand_search().send_keys("a")
        self.get_brand_search().send_keys(Keys.RETURN)
        print("Performed brand search")

    def click_retail_field(self):
        self.get_retail_field().click()
        self.get_retail_field().send_keys("99")
        print("Filled in the 'Retail' field")

    def click_retail_select_dropdown(self):
        self.get_retail_select_dropdown().click()
        print("Clicked on the 'Retail Select' dropdown")

    def click_select_search(self):
        self.get_select_search().click()
        self.get_select_search().send_keys(Keys.DOWN)
        self.get_select_search().send_keys(Keys.RETURN)
        print("Performed retail select search")

    def set_product_date(self):
        self.get_product_date().click()
        self.get_product_date().send_keys("12")
        self.get_product_date().send_keys("4")
        self.get_product_date().send_keys(Keys.RIGHT)
        self.get_product_date().send_keys("2025")
        print("Set the product date")

    def click_product_save_changes_button(self):
        self.get_product_save_changes_button().click()
        print("Clicked 'Save Changes' on product")

    def click_delete_product_button(self):
        self.get_delete_product_button().click()
        self.get_delete_product_confirmation().click()
        print("Clicked 'Delete Product' button")

    """Deals actions"""
    def click_deals(self):
        self.get_deals().click()
        print("Clicked on the 'Deals' tab")

    def set_deal_price(self):
        self.get_deal_price().click()
        self.get_deal_price().send_keys("99.99")
        print("Set the deal price")

    def click_deal_category_dropdown(self):
        self.get_deal_category().click()
        self.get_deal_category_search()
        self.get_deal_category_search().send_keys(Keys.DOWN)
        self.get_deal_category_search().send_keys(Keys.RETURN)
        print("Selected deal category from dropdown")

    def input_deal_url(self):
        self.get_deal_url().send_keys("https://demoqa.com/")
        print("Filled in the URL field")

    def set_deal_image(self):
        self.get_deal_image().click()
        self.get_image_option().click()
        self.get_image_option_confirm().click()
        print("Set the deal image")

    """FAQ actions"""
    def click_faq(self):
        self.get_faq().click()
        print("Clicked on the 'FAQ' tab")

    def input_faq_question(self):
        self.get_faq_question().send_keys("Test question")
        print("Filled in the question field")

    def input_faq_answer(self):
        iframe = self.driver.find_element(By.XPATH, '//iframe[@id="answer_ifr"]')
        self.driver.switch_to.frame(iframe)
        self.get_faq_answer().click()
        self.get_faq_answer().send_keys("Test answer")
        self.driver.switch_to.default_content()
        print("Filled in the answer field")

    """FAQ groups actions"""
    def click_faq_groups(self):
        self.get_faq_groups().click()
        print("Clicked on the 'FAQ Groups' tab")

    def click_faq_groups_name(self):
        self.get_faq_groups_name().click()
        self.get_faq_groups_name().send_keys("Test name")
        print("Filled in the group name field")

    """Model families actions"""
    def click_model_tab(self):
        self.get_model().click()
        print("Clicked on the 'Model Families' tab")

    # METHODS
    def attribute_groups_test(self):
        self.click_attribute_groups()
        self.click_new_attribute_button()
        self.input_name_attribute_field("test attribute group")
        self.click_input_sort_order()
        self.input_sort_order(Keys.BACKSPACE)
        self.input_sort_order("1")
        self.click_attribute_slider()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        self.assert_word(self.get_deleted_notification(), "deleted successfully")

    def attributes_tab_test(self):
        self.click_attributes()
        self.click_new_attribute_button()
        self.input_name_field("test attribute")
        self.click_type_dropdown()
        self.click_kind_checkbox()
        self.click_group_dropdown()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        self.assert_word(self.get_deleted_notification(), "deleted successfully")

    def ratings_tab_test(self):
        self.click_ratings()
        self.click_new_attribute_button()
        self.input_name_field("test rating")
        self.click_ratings_slider()
        self.click_speakers_checkbox()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        self.assert_word(self.get_deleted_notification(), "deleted successfully")

    def categories_tab_test(self):
        self.click_categories()
        self.click_new_attribute_button()
        self.input_name_field("test categorie")
        self.input_commission_field()
        self.click_headphones_radiobutton()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(1)

    def products_tab_test(self):
        self.click_get_products()
        self.click_new_attribute_button()
        self.input_name_field("test regress product")
        self.scroll_down(200)
        self.click_category_dropdown()
        self.click_category_option()
        self.driver.execute_script("document.querySelector('.phpdebugbar').style.display = 'none';")
        self.scroll_down(50)
        self.click_brand_dropdown()
        self.click_brand_search()
        self.click_retail_field()
        self.click_retail_select_dropdown()
        self.click_select_search()
        self.set_product_date()
        self.click_product_save_changes_button()
        self.assert_word(self.get_success_notification(), "saved successfully")
        self.click_delete_product_button()
        self.assert_word(self.get_product_deleted_notification(), "Deleted successfully")

    def deals_tab_test(self):
        self.click_deals()
        self.click_new_attribute_button()
        self.input_name_field("test deal")
        self.scroll_down(200)
        self.set_deal_price()
        self.click_deal_category_dropdown()
        self.input_deal_url()
        time.sleep(1)
        self.set_deal_image()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        self.assert_word(self.get_deleted_notification(), "deleted successfully")

    def faq_tab_test(self):
        self.click_faq()
        self.click_new_attribute_button()
        self.input_faq_question()
        self.input_faq_answer()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "Saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()

    def faq_group_tab_test(self):
        time.sleep(1)
        self.click_faq_groups()
        self.click_new_attribute_button()
        self.click_faq_groups_name()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()

    def model_tab_test(self):
        time.sleep(1)
        self.click_model_tab()
        self.click_new_attribute_button()
        self.click_faq_groups_name()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "Saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
















