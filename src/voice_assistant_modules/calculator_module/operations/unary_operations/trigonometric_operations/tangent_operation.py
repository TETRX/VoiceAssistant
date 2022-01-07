from src.voice_assistant_modules.calculator_module.operations.unary_operations.unary_operation import UnaryOperation
from math import tan


class TangentOperation(UnaryOperation):
    KEYWORDS = ("tangens z", "tangensa z")

    def calculate_one(self, arg):
        return tan(arg)
