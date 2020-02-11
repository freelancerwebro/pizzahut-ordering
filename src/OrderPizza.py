from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

class OrderPizza:
    logCounter = 0

    def __init__(self, config):
        self.config = config
        self.initDriver()

    def log(self, text):
        self.logCounter += 1
        print(str(self.logCounter) + ". " + text)

    def initDriver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(options=chrome_options)

    def acceptCookies(self):
        self.driver.get(self.config.getMyAccountUrl())
        self.log("Open pizzahutdelivery.ro")
        acceptCookies = self.driver.find_element_by_css_selector('a#CybotCookiebotDialogBodyLevelButtonAccept')
        acceptCookies.click()
        self.log("Accept cookies")

