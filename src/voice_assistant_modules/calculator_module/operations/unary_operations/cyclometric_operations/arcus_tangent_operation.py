from src.voice_assistant_modules.calculator_module.operations.unary_operations.cyclometric_operations.arcus_operation import \
    ArcusOperation
from src.voice_assistant_modules.calculator_module.operations.unary_operations.unary_operation import UnaryOperation
from math import atan


class ArcusTangentOperation(ArcusOperation):
    KEYWORDS = (
        "arcus tangens z",
        "arcusa tangensa z",
        "arcusa tangens z",
        "arcus tangensa z"
    )

    def calculate_one(self, arg):
        return atan(arg)
