from pages.products_section import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import allure
from utilities.logger import Logger


class FilmSection(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

    # LOCATORS
    """Genres tab locators"""
    FILMS = "//span[contains(text(), 'Films/TV')]"
    GENRES = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[11]"
    NEW_GENRE = "//a[contains(text(), 'New Genre')]"
    GENRE_NAME = "//input[@name='name']"

    """Age ratings locators"""
    AGE = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[12]"
    NEW_RATING = "//a[contains(text(), 'New Rating')]"
    MINIMAL_AGE = "//input[@type='number']"

    """Films locators"""
    FILM = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[13]"
    NEW_FILM = "//a[contains(text(), 'New Film')]"
    AGE_DROPDOWN = "(//div[@class='choices mb-0 flex-1'])[2]"
    AGE_SEARCH = "(//input[@type='search'])[2]"

    """Reviews locators"""
    REVIEW = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[14]"
    NEW_REVIEW = "//a[contains(text(), 'New Review')]"
    FILM_FIELD = "(//input[@class='border w-full rounded-md px-4 py-2'])[1]"
    TEST_FILM = "//a[contains(text(), 'Test film')]"
    TITLE_FIELD = "(//input[@class='border w-full rounded-md px-4 py-2'])[2]"
    RATING_FIELD = "(//input[@class='border w-full rounded-md px-4 py-2'])[4]"

    """People locators"""
    PEOPLE = "(//li[@class='text-white text-opacity-25 hover:text-opacity-100 pl-2'])[15]"
    NEW_PEOPLE = "//a[contains(text(), 'Add new')]"
    PEOPLE_SURNAME = "//input[@name='surname']"

    # GETTERS
    """Genre getters"""
    def get_films(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.FILMS)))

    def get_genres(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.GENRES)))

    def get_new_genre(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_GENRE)))

    def get_genre_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.GENRE_NAME)))

    """Age ratings getters"""
    def get_age(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.AGE)))

    def get_new_rating(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_RATING)))

    def get_minimal_age(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.MINIMAL_AGE)))

    """Films getters"""
    def get_film(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.FILM)))

    def get_new_film(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_FILM)))

    def get_age_dropdown(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.AGE_DROPDOWN)))

    def get_age_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.AGE_SEARCH)))

    """Reviews getters"""
    def get_review(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.REVIEW)))

    def get_new_review(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_REVIEW)))

    def get_film_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.FILM_FIELD)))

    def get_test_film(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.TEST_FILM)))

    def get_title_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.TITLE_FIELD)))

    def get_rating_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.RATING_FIELD)))

    """People getters"""
    def get_people(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.PEOPLE)))

    def get_new_people(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.NEW_PEOPLE)))

    def get_people_surname(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.PEOPLE_SURNAME)))

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
        with allure.step("genres tab test"):
            Logger.add_start_step(method="genres_tab_test")
            self.click_films()
            self.click_genres()
            self.click_new_genre()
            self.input_genre_name()
            self.click_save_changes_button()
            self.assert_word(self.get_success_notification(), "new item saved successfully")
            self.click_delete_item_button()
            self.click_delete_confirmation()
            Logger.add_end_step(url=self.driver.current_url, method="genres_tab_test")
            time.sleep(0.7)

    def age_tab_test(self):
        with allure.step("age tab test"):
            Logger.add_start_step(method="age_tab_test")
            self.click_age()
            self.click_new_rating()
            self.input_genre_name()
            self.input_minimal_age()
            self.click_save_changes_button()
            self.assert_word(self.get_success_notification(), "new item saved successfully")
            self.click_delete_item_button()
            self.click_delete_confirmation()
            Logger.add_end_step(url=self.driver.current_url, method="age_tab_test")
            time.sleep(0.7)

    def films_tab_test(self):
        with allure.step("films tab test"):
            Logger.add_start_step(method="films_tab_test")
            self.click_film()
            self.click_new_film()
            self.input_genre_name()
            self.click_age_dropdown()
            self.click_save_changes_button()
            self.assert_word(self.get_success_notification(), "saved successfully")
            self.click_delete_item_button()
            self.click_delete_confirmation()
            Logger.add_end_step(url=self.driver.current_url, method="films_tab_test")
            time.sleep(0.7)

    def reviews_tab_test(self):
        with allure.step("reviews tab test"):
            Logger.add_start_step(method="reviews_tab_test")
            self.click_review()
            self.click_new_review()
            self.input_film_field()
            self.input_title_field()
            self.input_rating_field()
            self.click_save_changes_button()
            self.click_delete_item_button()
            self.click_delete_confirmation()
            Logger.add_end_step(url=self.driver.current_url, method="reviews_tab_test")
            time.sleep(0.7)

    def people_tab_test(self):
        with allure.step("people tab test"):
            Logger.add_start_step(method="people_tab_test")
            self.click_people()
            self.click_new_people()
            self.input_genre_name()
            self.input_people_surname()
            self.click_save_changes_button()
            self.click_delete_item_button()
            self.click_delete_confirmation()
            Logger.add_end_step(url=self.driver.current_url, method="people_tab_test")



