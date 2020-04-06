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

    def __del__(self):
        time.sleep(5)
        self.driver.close()
        self.logger.p("Close browser")

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

    def login(self):
        usernameField = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//input[@name="email"]')))
        usernameField.send_keys(self.config.getUsername())
        passwordField = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//input[@name="password"]')))
        passwordField.send_keys(self.config.getPassword())
        usernameField.submit()
        self.logger.p("Log in")

    def addProductsToCart(self):
        self.logger.p("Add products to cart")
        defaultOrder = self.config.getDefaultOrder()
        for order in defaultOrder: 
            self.addProductToCart(order['product'], order['size'], order['base'])

    def addProductToCart(self, product, size, base):
        url = self.getProductUrl(product, size, base)
        self.driver.get(url)
        addToCart = self.driver.find_element_by_css_selector('a.product_order')
        addToCart.click()
        self.logger.p(" -> Product added to cart [" + product + " / " + size + " / " + base + "]")

    def getProductUrl(self, product, size = None, base = None):
        url = self.config.getBaseUrl() + "/pizza/pizza-" + product
        if size:
            url = url + "/size_" + size
        if base:
            url = url + "/base_" + base
        return url

    def checkout(self):
        self.driver.get(self.config.getCheckoutUrl())
        price = self.driver.find_element_by_css_selector('div#total_price span')

        self.logger.p("Checkout order [TOTAL = " + price.text + "]")
