from selenium import webdriver
import pytest

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()   #предусловие для открытия браузера перед тестом
    browser.maximize_window()      #предусловие для раскрытие на полное окно
    browser.implicitly_wait(3)     #ожидание 3 секунд для того, чтобы найти нужный элемент
    yield browser
    browser.close()     #постусловие для закрытия браузера после теста