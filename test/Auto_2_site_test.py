from selenium.webdriver.common.by import By
import time



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
