class Config:
    def __init__(self, config):
        self.config = config

    def getBaseUrl(self):
        return self.config.url['base']

    def getMyAccountUrl(self):
        return self.getBaseUrl() + self.config.url['my_account']
    
    def getCheckoutUrl(self):
        return self.getBaseUrl() + self.config.url['checkout']

    def getPaymentUrl(self):
        return self.getBaseUrl() + self.config.url['payment']

    def getUsername(self):
        return self.config.credentials['username']

    def getPassword(self):
        return self.config.credentials['password']

    def getDefaultOrder(self):
        return self.config.default_order['items']