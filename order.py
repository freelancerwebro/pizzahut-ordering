from src.Config import Config
from src.OrderPizza import OrderPizza
import src.config.core as configFile
from src.Logger import Logger

config = Config(configFile)
logger = Logger()
order = OrderPizza(config, logger)
order.acceptCookies()