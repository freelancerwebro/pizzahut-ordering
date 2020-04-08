from src.Config import Config
from src.OrderPizza import OrderPizza
from src.Driver import Driver
import src.config.core as configFile
from src.Logger import Logger

class OrderPizzaFacade:
    def init(self):
        config = Config(configFile)
        logger = Logger()
        driver = Driver.getInstance()

        order = OrderPizza(config, logger, driver)
        order.acceptCookies()
        order.login()
        order.addProductsToCart()
        order.goToCheckout()
        order.selectDeliveryTime()
        order.selectPaymentType()
        order.send()
