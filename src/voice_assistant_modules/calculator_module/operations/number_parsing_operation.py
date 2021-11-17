from src.voice_assistant_modules.calculator_module.operation import Operation

class NoNumberToParseException(Exception):
    pass

class NumberParsingOperation(Operation):
    @classmethod
    def get_keywords(cls):
        return []

    def calculate(self, *args):
        try:
            return self.parse(args[0])
        except IndexError:
            raise NoNumberToParseException

    def parse(self, text):
        return int(text)  # won't actually work, but goood enough for testing out the rest