import allure

from pages.other_section import OtherSection
from pages.os_section import OsSection
from pages.apps_section import AppsSection
from pages.products_section import MainPage
from pages.films_section import FilmSection
from pages.users_section import UserSection

@allure.description("Test products section")
def test_products_section(driver):
    print("Start checking products section")
    mp = MainPage(driver)
    mp.authorization()
    mp.attribute_groups_test()
    mp.attributes_tab_test()
    mp.ratings_tab_test()
    mp.categories_tab_test()
    mp.products_tab_test()
    mp.deals_tab_test()
    mp.faq_tab_test()
    mp.faq_group_tab_test()
    mp.model_tab_test()
    print("End checking products section")

@allure.description("Test films section")
def test_films_section(driver):
    print("Start checking Films/TV section")
    fs = FilmSection(driver)
    fs.authorization()
    fs.genres_tab_test()
    fs.age_tab_test()
    fs.films_tab_test()
    fs.reviews_tab_test()
    fs.people_tab_test()
    print("End checking Films/TV section")

@allure.description("Test os section")
def test_os_section(driver):
    print("Start checking OS section")
    os = OsSection(driver)
    os.authorization()
    os.licenses_tab_test()
    os.os_tab_test()
    print("End checking OS section")

@allure.description("Test users section")
def test_users_section(driver):
    print("Start checking users section")
    us = UserSection(driver)
    us.authorization()
    us.roles_tab_test()
    us.users_tab_test()
    us.domain_tab_test()
    print("End checking users section")

@allure.description("Test other section")
def test_other_section(driver):
    print("Start checking other section")
    ots = OtherSection(driver)
    ots.authorization()
    ots.other_tab_test()
    ots.app_stores_tab_test()
    ots.brands_tab_test()
    ots.countries_tab_test()
    ots.currencies_tab_test()
    ots.measure_tab_test()
    ots.websites_tab_test()
    ots.domains_tab_test()
    ots.badges_tab_test()
    ots.tags_tab_test()
    ots.deal_tags_test()
    print("End checking other section")

@allure.description("Test apps section")
def test_apps_section(driver):
    print("Start checking apps section")
    ap = AppsSection(driver)
    ap.authorization()
    ap.apps_tab_test()
    print("End checking apps section")