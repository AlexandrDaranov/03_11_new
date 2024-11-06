from selenium.webdriver.common.by import By

class HomePage:


    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get('https://demoblaze.com/index.html')


    def iphone_6(self):
        iphone_6 = self.browser.find_element(By.XPATH, value='//a[text()="Iphone 6 32gb"]')
        iphone_6.click()
