from src.voice_assistant_modules.calculator_module.operations.binary_operations.binary_operation import BinaryOperation


def minus(binary_operation):
    class MinusBinaryOperation(binary_operation):
        @classmethod
        def get_keywords(cls):
            return tuple([keyword + " minus" for keyword in binary_operation.get_keywords()])

        def calculate_two(self, arg1, arg2):
            return super().calculate_two(arg1, -arg2)