import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def base_url():
    base_url_login = 'https://qa-guru.github.io/one-page-form/login.html'
    return base_url_login


@pytest.fixture
def driver_login():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_tc_01(base_url, driver_login):
    driver = driver_login
    driver.get(base_url)
    login_field = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[1]/label')
    password_field = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[2]/label')
    assert login_field.text == 'Login'
    assert password_field.text == 'Password'


def test_tc_02(base_url, driver_login):
    driver_login.get(base_url)
    login_field = driver_login.find_element(By.ID, 'login-input')
    password_field = driver_login.find_element(By.ID, 'password-input')
    login_field.send_keys('user1')
    password_field.send_keys('password1')
    login_button = driver_login.find_element(By.ID, 'submit-button')
    login_button.click()
    welcome_message = driver_login.find_element(By.ID, 'welcome-message').text
    assert welcome_message == 'Welcome, user1!'


def test_tc_03(base_url, driver_login):
    driver_login.get(base_url)
    login_field = driver_login.find_element(By.ID, 'login-input')
    password_field = driver_login.find_element(By.ID, 'password-input')
    login_field.send_keys('user1_fail')
    password_field.send_keys('password1')
    login_button = driver_login.find_element(By.ID, 'submit-button')
    login_button.click()
    error_message = driver_login.find_element(By.ID, 'error-message').text
    assert error_message == 'Wrong login or password'

def test_tc_04(base_url, driver_login):
    driver_login.get(base_url)
    login_field = driver_login.find_element(By.ID, 'login-input')
    password_field = driver_login.find_element(By.ID, 'password-input')
    login_field.send_keys('user1')
    password_field.send_keys('password1_fail')
    login_button = driver_login.find_element(By.ID, 'submit-button')
    login_button.click()
    error_message = driver_login.find_element(By.ID, 'error-message').text
    assert error_message == 'Wrong login or password'

def test_tc_05(base_url, driver_login):
    driver_login.get(base_url)
    login_field = driver_login.find_element(By.ID, 'login-input')
    password_field = driver_login.find_element(By.ID, 'password-input')
    login_field.send_keys('user1_fail')
    password_field.send_keys('password1_fail')
    login_button = driver_login.find_element(By.ID, 'submit-button')
    login_button.click()
    error_message = driver_login.find_element(By.ID, 'error-message').text
    assert error_message == 'Wrong login or password'

def test_tc_06(base_url, driver_login):
    driver_login.get(base_url)
    login_field = driver_login.find_element(By.ID, 'login-input')
    password_field = driver_login.find_element(By.ID, 'password-input')
    login_field.send_keys('')
    password_field.send_keys('')
    login_button = driver_login.find_element(By.ID, 'submit-button')
    login_button.click()
    error_message = driver_login.find_element(By.ID, 'error-message').text
    assert error_message == 'Login and password are required (minimum 3 and 6 characters)'

def test_tc_07(base_url, driver_login):
    driver_login.get(base_url)
    login_field = driver_login.find_element(By.ID, 'login-input')
    password_field = driver_login.find_element(By.ID, 'password-input')
    login_field.send_keys('')
    password_field.send_keys('password1')
    login_button = driver_login.find_element(By.ID, 'submit-button')
    login_button.click()
    error_message = driver_login.find_element(By.ID, 'error-message').text
    assert error_message == 'Login is required (minimum 3 characters)'

def test_tc_08(base_url, driver_login):
    driver_login.get(base_url)
    login_field = driver_login.find_element(By.ID, 'login-input')
    password_field = driver_login.find_element(By.ID, 'password-input')
    login_field.send_keys('user1')
    password_field.send_keys('')
    login_button = driver_login.find_element(By.ID, 'submit-button')
    login_button.click()
    error_message = driver_login.find_element(By.ID, 'error-message').text
    assert error_message == 'Password is required (minimum 6 characters)'

def test_tc_09(base_url, driver_login):
    driver_login.get(base_url)
    login_field = driver_login.find_element(By.ID, 'login-input')
    password_field = driver_login.find_element(By.ID, 'password-input')
    login_field.send_keys('user 1')
    password_field.send_keys('password1')
    login_button = driver_login.find_element(By.ID, 'submit-button')
    login_button.click()
    error_message = driver_login.find_element(By.ID, 'error-message').text
    assert error_message == 'Wrong login or password'

def test_tc_10(base_url, driver_login):
    driver_login.get(base_url)
    login_field = driver_login.find_element(By.ID, 'login-input')
    password_field = driver_login.find_element(By.ID, 'password-input')
    login_field.send_keys('user1')
    password_field.send_keys('pas swo rd1')
    login_button = driver_login.find_element(By.ID, 'submit-button')
    login_button.click()
    error_message = driver_login.find_element(By.ID, 'error-message').text
    assert error_message == 'Wrong login or password'

def test_tc_11(base_url, driver_login):
    driver_login.get(base_url)
    login_field = driver_login.find_element(By.ID, 'login-input')
    password_field = driver_login.find_element(By.ID, 'password-input')
    login_field.send_keys('user1')
    password_field.send_keys('password1')
    login_button = driver_login.find_element(By.ID, 'submit-button')
    login_button.click()
    logout_button = driver_login.find_element(By.ID, 'logout-button')
    assert logout_button.is_displayed()
    logout_button.click()
    login_field = driver_login.find_element(By.XPATH, '//*[@id="login-form"]/div[1]/label')
    password_field = driver_login.find_element(By.XPATH, '//*[@id="login-form"]/div[2]/label')
    assert login_field.text == 'Login'
    assert password_field.text == 'Password'


def test_tc_12(base_url, driver_login):
    driver_login.get(base_url)
    login_field = driver_login.find_element(By.ID, 'login-input')
    password_field = driver_login.find_element(By.ID, 'password-input')
    login_field.send_keys('user1')
    password_field.send_keys('password1')
    login_button = driver_login.find_element(By.ID, 'submit-button')
    login_button.click()
    logout_button = driver_login.find_element(By.ID, 'logout-button')
    assert logout_button.is_displayed()
    logout_button.click()
    login_field = driver_login.find_element(By.XPATH, '//*[@id="login-form"]/div[1]/label')
    password_field = driver_login.find_element(By.XPATH, '//*[@id="login-form"]/div[2]/label')
    assert login_field.text == 'Login'
    assert password_field.text == 'Password'
    login_field = driver_login.find_element(By.ID, 'login-input')
    password_field = driver_login.find_element(By.ID, 'password-input')
    login_field.send_keys('user1')
    password_field.send_keys('password1')
    login_button = driver_login.find_element(By.ID, 'submit-button')
    login_button.click()
    welcome_message = driver_login.find_element(By.ID, 'welcome-message').text
    assert welcome_message == 'Welcome, user1!'

