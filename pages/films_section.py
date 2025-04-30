from pages.products_section import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

class FilmSection(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS
    """Genres tab locators"""
    films = "//span[contains(text(), 'Films/TV')]"
    genres = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[10]"
    new_genre = "//a[contains(text(), 'New Genre')]"
    genre_name = "//input[@name='name']"

    """Age ratings locators"""
    age = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[11]"
    new_rating = "//a[contains(text(), 'New Rating')]"
    minimal_age = "//input[@type='number']"

    """Films locators"""
    film = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[12]"
    new_film = "//a[contains(text(), 'New Film')]"
    age_dropdown = "(//div[@class='choices mb-0 flex-1'])[2]"
    age_search = "(//input[@type='search'])[2]"

    """Reviews locators"""
    review = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[13]"
    new_review = "//a[contains(text(), 'New Review')]"
    film_field = "(//input[@class='border w-full rounded-md px-4 py-2'])[1]"
    test_film = "//a[contains(text(), 'Test film')]"
    title_field = "(//input[@class='border w-full rounded-md px-4 py-2'])[2]"
    rating_field = "(//input[@class='border w-full rounded-md px-4 py-2'])[4]"

    """People locators"""
    people = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[14]"
    new_people = "//a[contains(text(), 'Add new')]"
    people_surname = "//input[@name='surname']"

    # GETTERS
    """Genre getters"""
    def get_films(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.films)))

    def get_genres(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.genres)))

    def get_new_genre(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_genre)))

    def get_genre_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.genre_name)))

    """Age ratings getters"""
    def get_age(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.age)))

    def get_new_rating(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_rating)))

    def get_minimal_age(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.minimal_age)))

    """Films getters"""
    def get_film(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.film)))

    def get_new_film(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_film)))

    def get_age_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.age_dropdown)))

    def get_age_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.age_search)))

    """Reviews getters"""
    def get_review(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.review)))

    def get_new_review(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_review)))

    def get_film_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.film_field)))

    def get_test_film(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.test_film)))

    def get_title_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_field)))

    def get_rating_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.rating_field)))

    """People getters"""
    def get_people(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.people)))

    def get_new_people(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_people)))

    def get_people_surname(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.people_surname)))

    # ACTIONS
    """Genre actions"""
    def click_films(self):
        self.get_films().click()
        print("Clicked on the films tab")

    def click_genres(self):
        self.get_genres().click()
        print("Clicked on the genres tab")

    def click_new_genre(self):
        self.get_new_genre().click()
        print("Clicked on the new genre button")

    def input_genre_name(self):
        self.get_genre_name().send_keys("Test name")
        print("Filled in genre name")

    """Age ratings actions"""
    def click_age(self):
        self.get_age().click()
        print("Clicked on the age tab")

    def click_new_rating(self):
        self.get_new_rating().click()
        print("Clicked on the new rating button")

    def input_minimal_age(self):
        self.get_minimal_age().click()
        self.get_minimal_age().send_keys(Keys.BACKSPACE)
        self.get_minimal_age().send_keys("18")
        print("Filled in minimal age")

    """Films actions"""
    def click_film(self):
        self.get_film().click()
        print("Clicked on the films tab")

    def click_new_film(self):
        self.get_new_film().click()
        print("Clicked on the new film button")

    def click_age_dropdown(self):
        self.get_age_dropdown().click()
        self.get_age_search().click()
        self.get_age_search().send_keys(Keys.DOWN)
        self.get_age_search().send_keys(Keys.RETURN)
        print("Clicked on the age dropdown")

    """Reviews actions"""
    def click_review(self):
        self.get_review().click()
        print("Clicked on the review tab")

    def click_new_review(self):
        self.get_new_review().click()
        print("Clicked on the new review button")

    def input_film_field(self):
        self.get_film_field().send_keys("T")
        self.get_test_film().click()
        print("Filled in film field")

    def input_title_field(self):
        self.get_title_field().send_keys("Test title")
        print("Filled in title field")

    def input_rating_field(self):
        self.get_rating_field().send_keys("18")
        print("Filled in rating field")

    """People actions"""
    def click_people(self):
        self.get_people().click()
        print("Clicked on the people tab")

    def click_new_people(self):
        self.get_new_people().click()
        print("Clicked on the new people button")

    def input_people_surname(self):
        self.get_people_surname().send_keys("Test surname")
        print("Clicked on the new people button")


    # METHODS
    def genres_tab_test(self):
        self.click_films()
        self.click_genres()
        self.click_new_genre()
        self.input_genre_name()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def age_tab_test(self):
        self.click_age()
        self.click_new_rating()
        self.input_genre_name()
        self.input_minimal_age()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "new item saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def films_tab_test(self):
        self.click_film()
        self.click_new_film()
        self.input_genre_name()
        self.click_age_dropdown()
        self.click_save_changes_button()
        self.assert_word(self.get_success_notification(), "saved successfully")
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def reviews_tab_test(self):
        self.click_review()
        self.click_new_review()
        self.input_film_field()
        self.input_title_field()
        self.input_rating_field()
        self.click_save_changes_button()
        self.click_delete_item_button()
        self.click_delete_confirmation()
        time.sleep(0.7)

    def people_tab_test(self):
        self.click_people()
        self.click_new_people()
        self.input_genre_name()
        self.input_people_surname()
        self.click_save_changes_button()
        self.click_delete_item_button()
        self.click_delete_confirmation()
        


