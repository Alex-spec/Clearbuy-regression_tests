import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    # Browser settings
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    #  Launch WebDriver
    driver = webdriver.Chrome(
        options=options,
        service=ChromeService(ChromeDriverManager().install())
    )

    yield driver

    # Close the browser after the test
    print("End test")
    driver.quit()


