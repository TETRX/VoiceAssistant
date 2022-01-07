from src.voice_assistant_modules.calculator_module.operations.unary_operations.unary_operation import UnaryOperation
from math import log10


class BinaryLogOperation(UnaryOperation):
    KEYWORDS = (
        "logarytm binarny z",
        "logarytmu binarnego z",
        "logarytm dwójkowy z",
        "logarytmu dwójkowego z"
    )

    def calculate_one(self, arg):
        return log10(arg)

