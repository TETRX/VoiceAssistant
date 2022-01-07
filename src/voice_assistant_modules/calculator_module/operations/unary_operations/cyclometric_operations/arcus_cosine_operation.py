from src.voice_assistant_modules.calculator_module.operations.unary_operations.cyclometric_operations.arcus_operation import \
    ArcusOperation
from src.voice_assistant_modules.calculator_module.operations.unary_operations.unary_operation import UnaryOperation
from math import acos


class ArcusCosineOperation(ArcusOperation):
    KEYWORDS = (
        "arcus cosinus z",
        "arcusa cosinusa z",
        "arcus cosinusa z",
        "arcusa cosinus z"
    )

    def calculate_one(self, arg):
        return acos(arg)
