# Пока мы покрываем тестами 2 страницы:
# https://qa-guru.github.io/one-page-form/text-box.html
# https://qa-guru.github.io/one-page-form/login.html
# с помощью Chrome DevTools изучить верстку страницы (AUT);
# Успешно изменить входные данные тестов;
# По аналогии разработать тесты с другими данными и результатами (позитивные, негативные сценарии  - заведомо неправильный email без собачки, пустой, слишком длинный, с запрещенными спецсимволами, SQL, JSON любая другая инъекция как удар по безопасности);
# Разработать тесты с использованием всех возможных полей;

import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


# base_url_text_box = 'https://qa-guru.github.io/one-page-form/text-box.html'
@pytest.fixture
def base_url():
    base_url_login = 'https://qa-guru.github.io/one-page-form/login.html'
    return base_url_login

@pytest.fixture
def driver_login():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Happy Pass
def test_login(base_url,driver_login):
    print('Открываем сайт')
    driver_login.get(base_url)
    time.sleep(3)
    print('Вводим правильные тестовые данные')
    login_field = driver_login.find_element(By.ID, 'login-input')
    password_field = driver_login.find_element(By.ID, 'password-input')
    login_field.send_keys('user1')
    password_field.send_keys('password1')
    print('Жмем на кнопку ввода')
    login_button = driver_login.find_element(By.ID, 'submit-button')
    login_button.click()
    time.sleep(5)
    print('Сравниваем приветственное сообщение')
    welcome_message = driver_login.find_element(By.ID, 'welcome-message').text
    assert welcome_message == 'Welcome, user1!'




