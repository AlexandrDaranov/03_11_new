#from distutils.command.install import value

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()   #предусловие для открытия браузера перед тестом
    browser.maximize_window()      #предусловие для раскрытие на полное окно
    browser.implicitly_wait(3)     #ожидание 3 секунд для того, чтобы найти нужный элемент
    yield browser
    browser.close()     #постусловие для закрытия браузера после теста

def test_open_ip6(browser):
    browser.get('https://demoblaze.com/index.html')
    iphone_6 = browser.find_element(By.XPATH, value = '//a[text()="Iphone 6 32gb"]')
    iphone_6.click()
    title = browser.find_element(By.CSS_SELECTOR, value = 'h2')
    assert title.text == 'Iphone 6 32gb'
