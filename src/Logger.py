class Logger:
    counter = 0

    def p(self, text):
        self.counter += 1
        print(str(self.counter) + ". " + text)