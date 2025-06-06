import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.base_methods import BasePage
from pages.products_section import ProductsSectionSteps
from utilities.logger import Logger

class FilmsSectionLocators:

    # Genres tab locators
    FILMS = (By.XPATH, "//span[contains(text(), 'Films/TV')]")
    GENRES = (By.XPATH, "//a[text()='Genres']")
    NEW_GENRE = (By.XPATH, "//a[contains(text(), 'New Genre')]")
    GENRE_NAME = (By.XPATH, "//input[@name='name']")

    # Age ratings locators
    AGE = (By.XPATH, "//a[text()='Age ratings']")
    NEW_RATING = (By.XPATH, "//a[contains(text(), 'New Rating')]")
    MINIMAL_AGE = (By.XPATH, "//input[@type='number']")

    # Films locators
    FILM = (By.XPATH, "//a[text()='Films']")
    NEW_FILM = (By.XPATH, "//a[contains(text(), 'New Film')]")
    AGE_DROPDOWN = (By.XPATH, "(//div[@class='choices mb-0 flex-1'])[2]")
    AGE_SEARCH = (By.XPATH, "(//input[@type='search'])[2]")

    # Reviews locators
    REVIEW = (By.XPATH, "//a[text()='Reviews']")
    NEW_REVIEW = (By.XPATH, "//a[contains(text(), 'New Review')]")
    FILM_FIELD = (By.XPATH, "(//input[@class='border w-full rounded-md px-4 py-2'])[1]")
    TEST_FILM = (By.XPATH, "//a[contains(text(), 'Test film')]")
    TITLE_FIELD = (By.XPATH, "(//input[@class='border w-full rounded-md px-4 py-2'])[2]")
    RATING_FIELD = (By.XPATH, "(//input[@class='border w-full rounded-md px-4 py-2'])[4]")

    # People locators
    PEOPLE = (By.XPATH, "//a[text()='People']")
    NEW_PEOPLE = (By.XPATH, "//a[contains(text(), 'Add new')]")
    PEOPLE_SURNAME = (By.XPATH, "//input[@name='surname']")

class FilmsSectionGetters(BasePage):

    # Genre getters

    def get_films(self):
        return self.wait_for_clickable(FilmsSectionLocators.FILMS)

    def get_genres(self):
        return self.wait_for_clickable(FilmsSectionLocators.GENRES)

    def get_new_genre(self):
        return self.wait_for_clickable(FilmsSectionLocators.NEW_GENRE)

    def get_genre_name(self):
        return self.wait_for_clickable(FilmsSectionLocators.GENRE_NAME)

    # Age ratings getters

    def get_age(self):
        return self.wait_for_clickable(FilmsSectionLocators.AGE)

    def get_new_rating(self):
        return self.wait_for_clickable(FilmsSectionLocators.NEW_RATING)

    def get_minimal_age(self):
        return self.wait_for_clickable(FilmsSectionLocators.MINIMAL_AGE)

    # Films getters

    def get_film(self):
        return self.wait_for_clickable(FilmsSectionLocators.FILM)

    def get_new_film(self):
        return self.wait_for_clickable(FilmsSectionLocators.NEW_FILM)

    def get_age_dropdown(self):
        return self.wait_for_clickable(FilmsSectionLocators.AGE_DROPDOWN)

    def get_age_search(self):
        return self.wait_for_clickable(FilmsSectionLocators.AGE_SEARCH)

    # Reviews getters

    def get_review(self):
        return self.wait_for_clickable(FilmsSectionLocators.REVIEW)

    def get_new_review(self):
        return self.wait_for_clickable(FilmsSectionLocators.NEW_REVIEW)

    def get_film_field(self):
        return self.wait_for_clickable(FilmsSectionLocators.FILM_FIELD)

    def get_test_film(self):
        return self.wait_for_clickable(FilmsSectionLocators.TEST_FILM)

    def get_title_field(self):
        return self.wait_for_clickable(FilmsSectionLocators.TITLE_FIELD)

    def get_rating_field(self):
        return self.wait_for_clickable(FilmsSectionLocators.RATING_FIELD)

    # People getters

    def get_people(self):
        return self.wait_for_clickable(FilmsSectionLocators.PEOPLE)

    def get_new_people(self):
        return self.wait_for_clickable(FilmsSectionLocators.NEW_PEOPLE)

    def get_people_surname(self):
        return self.wait_for_clickable(FilmsSectionLocators.PEOPLE_SURNAME)

class FilmsSectionActions(FilmsSectionGetters):

    # Genre actions
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

    # Age ratings actions

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

    # Films actions
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

    # Reviews actions

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

    # People actions
    def click_people(self):
        self.get_people().click()
        print("Clicked on the people tab")

    def click_new_people(self):
        self.get_new_people().click()
        print("Clicked on the new people button")

    def input_people_surname(self):
        self.get_people_surname().send_keys("Test surname")
        print("Clicked on the new people button")

class FilmsSectionSteps(FilmsSectionActions, ProductsSectionSteps):

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
            time.sleep(1)



