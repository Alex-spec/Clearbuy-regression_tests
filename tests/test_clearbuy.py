import allure

from pages.apps_section import AppsSectionSteps
from pages.films_section import FilmsSectionSteps
from pages.os_section import OsSectionSteps
from pages.other_section import OtherSectionSteps
from pages.products_section import ProductsSectionSteps
from pages.users_section import UsersSectionSteps


@allure.description("Test products section")
def test_products_section(driver):
    print("Start checking products section")
    ps = ProductsSectionSteps(driver)
    ps.attribute_groups_test()
    ps.attributes_tab_test()
    ps.ratings_tab_test()
    ps.categories_tab_test()
    ps.products_tab_test()
    ps.deals_tab_test()
    ps.faq_tab_test()
    ps.faq_group_tab_test()
    ps.model_tab_test()
    print("End checking products section")

@allure.description("Test films section")
def test_films_section(driver):
    print("Start checking Films/TV section")
    fs = FilmsSectionSteps(driver)
    fs.genres_tab_test()
    fs.age_tab_test()
    fs.films_tab_test()
    fs.reviews_tab_test()
    fs.people_tab_test()
    print("End checking Films/TV section")

@allure.description("Test os section")
def test_os_section(driver):
    print("Start checking OS section")
    os = OsSectionSteps(driver)
    os.licenses_tab_test()
    os.os_tab_test()
    print("End checking OS section")

@allure.description("Test users section")
def test_users_section(driver):
    print("Start checking users section")
    us = UsersSectionSteps(driver)
    us.roles_tab_test()
    us.users_tab_test()
    us.domain_tab_test()
    print("End checking users section")

@allure.description("Test other section")
def test_other_section(driver):
    print("Start checking other section")
    ots = OtherSectionSteps(driver)
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
    ap = AppsSectionSteps(driver)
    ap.apps_tab_test()
    print("End checking apps section")