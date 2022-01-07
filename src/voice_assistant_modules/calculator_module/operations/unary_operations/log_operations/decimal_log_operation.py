from src.voice_assistant_modules.calculator_module.operations.unary_operations.unary_operation import UnaryOperation
from math import log10


class DecimalLogOperation(UnaryOperation):
    KEYWORDS = (
        "logarytm dziesiętny z",
        "logarytmu dziesiętnego z"
    )

    def calculate_one(self, arg):
        return log10(arg)

