from selenium import webdriver
from src.Driver.DriverInterface import DriverInterface

class ChromeDriver(DriverInterface):
    @staticmethod
    def getInstance():
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('headless')
        return webdriver.Chrome(options=chrome_options)