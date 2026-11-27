import pytest
from selenium import webdriver

@pytest.fixture
def base_url():
    base_url_login = 'https://qa-guru.github.io/one-page-form/login.html'
    return base_url_login


@pytest.fixture
def driver_login():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()