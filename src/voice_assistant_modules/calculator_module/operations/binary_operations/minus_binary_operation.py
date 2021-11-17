from src.voice_assistant_modules.calculator_module.operations.binary_operations.binary_operation import BinaryOperation


class Minus:
    ALREADY_DEFINED_MINUSES = {}

    @classmethod
    def minus(cls, binary_operation):
        if binary_operation in cls.ALREADY_DEFINED_MINUSES:
            return cls.ALREADY_DEFINED_MINUSES[binary_operation]

        class MinusBinaryOperation(binary_operation):
            @classmethod
            def get_keywords(cls):
                return [keyword + " minus" for keyword in binary_operation.get_keywords()]

            def calculate_two(self, arg1, arg2):
                return super().calculate_two(arg1, -arg2)

        cls.ALREADY_DEFINED_MINUSES[binary_operation] = MinusBinaryOperation
        return cls.ALREADY_DEFINED_MINUSES[binary_operation]
