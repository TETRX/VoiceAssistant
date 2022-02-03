import abc

from src.voice_assistant_modules.calculator_module.operation import Operation


class UnaryOperation(Operation, abc.ABC):
    KEYWORDS = ()

    @abc.abstractmethod
    def calculate_one(self, arg):
        pass

    def calculate(self, *args):
        return_value = args[-1]
        for i in range(len(args)-1):
            return_value = self.calculate_one(return_value)
        return return_value

    @classmethod
    def get_keywords(cls):
        return cls.KEYWORDS
