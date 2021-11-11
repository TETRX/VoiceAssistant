from src.voice_assistant_modules.calculator_module.operations.binary_operations.binary_operation import BinaryOperation


class SubtractionOperation(BinaryOperation):
    KEYWORDS = (
        "minus",
        "odjąć",
        "odejmij"
    )

    def calculate_two(self, arg1, arg2):
        return arg1 - arg2

    @classmethod
    def get_keywords(cls):
        return cls.KEYWORDS
