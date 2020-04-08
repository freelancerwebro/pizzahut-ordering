from selenium import webdriver

class Driver:
    @staticmethod
    def getInstance():
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('headless')
        return webdriver.Chrome(options=chrome_options)
