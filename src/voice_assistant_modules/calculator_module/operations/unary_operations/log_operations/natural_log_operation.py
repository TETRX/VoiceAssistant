from src.voice_assistant_modules.calculator_module.operations.unary_operations.unary_operation import UnaryOperation
from math import log


class NaturalLogOperation(UnaryOperation):
    KEYWORDS = (
        "logarytm z",
        "logarytmu z",
        "logarytm naturalny z",
        "logarytmu naturalnego z"
    )

    def calculate_one(self, arg):
        return log(arg)

