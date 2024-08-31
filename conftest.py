import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    # Setup: Initialize the WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Use headless mode if running in CI
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)


    # Return the driver to be used in tests
    yield driver

    # Teardown: Quit the WebDriver
    driver.quit()
