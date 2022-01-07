from src.voice_assistant_modules.calculator_module.operations.unary_operations.unary_operation import UnaryOperation
from mpmath import cot


class CotangentOperation(UnaryOperation):
    KEYWORDS = ("cotangens z", "cotangensa z")

    def calculate_one(self, arg):
        return cot(arg)
