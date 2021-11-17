from src.voice_assistant_modules.calculator_module.operations.binary_operations.binary_operation import BinaryOperation


class DivisionOperation(BinaryOperation):
    KEYWORDS = (
        "podzielone przez",
        "podzielić przez",
        "podzielić",
        "podziel",
        "przez",
    )

    def calculate_two(self, arg1, arg2):
        return arg1 / arg2

    @classmethod
    def get_keywords(cls):
        return cls.KEYWORDS
