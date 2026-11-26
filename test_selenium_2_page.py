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

driver = webdriver.Chrome

base_url_text_box = 'https://qa-guru.github.io/one-page-form/text-box.html'
base_url_login = 'https://qa-guru.github.io/one-page-form/login.html'

def test_login(base_url):
    base_url = base_url_login
    print('Открываем сайт')
    driver.get(base_url)
    time.sleep(3)
    driver.quit()

test_login()