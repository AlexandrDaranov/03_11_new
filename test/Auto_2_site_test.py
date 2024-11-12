from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()   #предусловие для открытия браузера перед тестом
    browser.maximize_window()      #предусловие для раскрытие на полное окно
    browser.implicitly_wait(3)     #ожидание 3 секунд для того, чтобы найти нужный элемент
    yield browser
    browser.close()     #постусловие для закрытия браузера после теста


def test_open_ip6(browser):                        #Проверка названия карточки на доп странице
    browser.get('https://demoblaze.com/index.html')
    iphone_6 = browser.find_element(By.XPATH, value = '//a[text()="Iphone 6 32gb"]')
    iphone_6.click()
    title = browser.find_element(By.CSS_SELECTOR, value = 'h2')
    assert title.text == 'Iphone 6 32gb'

def test_two_monitors(browser):                     #Проверка наличия 2 карточек сразу на доп странице
    browser.get('https://demoblaze.com/index.html')
    monitor_link = browser.find_element(By.CSS_SELECTOR, value = '''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(2) #это крайняя мера, в других случ. исп. конкретное ожидание чего-то
    monitors = browser.find_elements(By.CSS_SELECTOR, value = ".card")
    assert len(monitors) == 2
