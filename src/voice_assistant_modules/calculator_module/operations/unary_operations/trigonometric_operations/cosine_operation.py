from src.voice_assistant_modules.calculator_module.operations.unary_operations.unary_operation import UnaryOperation
from math import cos


class CosineOperation(UnaryOperation):
    KEYWORDS = ("cosinus z", "cosinusa z")

    def calculate_one(self, arg):
        return cos(arg)
