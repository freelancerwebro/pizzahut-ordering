from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time

class OrderPizza:
    logger = None

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.initDriver()

    def initDriver(self):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('headless')
        self.driver = webdriver.Chrome(options=chrome_options)

    def acceptCookies(self):
        self.driver.get(self.config.getMyAccountUrl())
        time.sleep(5)
        self.logger.p("Open pizzahutdelivery.ro")
        acceptCookies = self.driver.find_element_by_css_selector('a#CybotCookiebotDialogBodyLevelButtonAccept')
        acceptCookies.click()
        self.logger.p("Accept cookies")

    def __del__(self):
        time.sleep(5)
        self.driver.close()
        self.logger.p("Close browser")

