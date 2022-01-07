from src.voice_assistant_modules.calculator_module.operations.unary_operations.cyclometric_operations.arcus_operation import \
    ArcusOperation
from src.voice_assistant_modules.calculator_module.operations.unary_operations.unary_operation import UnaryOperation
from mpmath import acot


class ArcusCotangentOperation(ArcusOperation):
    KEYWORDS = (
        "arcus cotangens z",
        "arcusa cotangensa z",
        "arcus cotangensa z",
        "arcusa cotangensa z"
    )

    def calculate_one(self, arg):
        return acot(arg)
