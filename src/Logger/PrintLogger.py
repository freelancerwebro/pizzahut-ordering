from src.Logger.LoggerInterface import LoggerInterface

class PrintLogger(LoggerInterface):
    counter = 0

    def p(self, text: str) -> None:
        self.counter += 1
        print(str(self.counter) + ". " + text)