from src.Config import Config
from src.OrderPizza import OrderPizza
import src.config.core as configFile


config = Config(configFile)
order = OrderPizza(config)

order.acceptCookies()