from src.voice_assistant_modules.calculator_module.operations.unary_operations.unary_operation import UnaryOperation
from math import sin


class SineOperation(UnaryOperation):
    KEYWORDS = ("sinus z", "sinusa z")

    def calculate_one(self, arg):
        return sin(arg)
