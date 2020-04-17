from src.Config import Config
from src.OrderPizza import OrderPizza
import src.config.core as configFile
from src.Logger.PrintLogger import PrintLogger
from src.Driver.ChromeDriver import ChromeDriver

class OrderPizzaFacade:
    def init(self):
        config = Config(configFile)
        logger = PrintLogger()
        driver = ChromeDriver.getInstance()

        order = OrderPizza(config, logger, driver)
        order.acceptCookies()
        order.login()
        order.addProductsToCart()
        order.goToCheckout()
        order.selectDeliveryTime()
        order.selectPaymentType()
        order.send()
