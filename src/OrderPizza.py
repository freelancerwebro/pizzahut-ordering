from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time

class OrderPizza:
    logger = None
    waitTimer = 5

    def __init__(self, config, logger, driver):
        self.config = config
        self.logger = logger
        self.driver = driver

    def __del__(self):
        time.sleep(5)
        self.driver.close()
        self.logger.p("Close browser")

    def acceptCookies(self):
        self.driver.get(self.config.getMyAccountUrl())
        time.sleep(5)
        self.logger.p("Open pizzahutdelivery.ro")
        acceptCookies = self.driver.find_element_by_css_selector('a#CybotCookiebotDialogBodyLevelButtonAccept')
        acceptCookies.click()
        self.logger.p("Accept cookies")

    def login(self):
        usernameField = WebDriverWait(self.driver, self.waitTimer).until(EC.element_to_be_clickable((By.XPATH,'//input[@name="email"]')))
        usernameField.send_keys(self.config.getUsername())
        passwordField = WebDriverWait(self.driver, self.waitTimer).until(EC.element_to_be_clickable((By.XPATH,'//input[@name="password"]')))
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

    def goToCheckout(self):
        self.driver.get(self.config.getCheckoutUrl())
        time.sleep(5)
        price = self.driver.find_element_by_css_selector('div#total_price span')
        self.logger.p("Checkout order [TOTAL = " + price.text + "]")

    def selectDeliveryTime(self):
        deliveryTime = self.config.getDeliveryTime()
        selectTime = self.driver.find_element_by_css_selector('div.checkout_selection .otime_' + deliveryTime)
        selectTime.click()

        continueOrder = self.driver.find_element_by_css_selector('a.checkout_step2_bt')
        continueOrder.click()
        self.logger.p("Select delivery time [" + deliveryTime + "]")

    def selectPaymentType(self):
        time.sleep(5)
        paymentType = self.config.getPaymentType()
        payment = self.driver.find_element_by_css_selector('div#pay_' + str(paymentType))
        payment.click()

        paymentTypeStr = self.config.getPaymentById(paymentType)
        self.logger.p("Select payment type [" + paymentTypeStr + "]")

    def send(self):
        send = self.driver.find_element_by_css_selector('a.checkout_step3_bt')
        # send.click()
        self.logger.p("Place order")