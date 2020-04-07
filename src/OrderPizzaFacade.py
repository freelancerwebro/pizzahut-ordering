from src.Config import Config
from src.OrderPizza import OrderPizza
import src.config.core as configFile
from src.Logger import Logger

class OrderPizzaFacade:
	def init(self):
		config = Config(configFile)
		logger = Logger()

		order = OrderPizza(config, logger)
		order.acceptCookies()
		order.login()
		order.addProductsToCart()
		order.goToCheckout()
		order.selectDeliveryTime()
		order.selectPaymentType()
		order.send()
