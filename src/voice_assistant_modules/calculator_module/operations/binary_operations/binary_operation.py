import abc

from src.voice_assistant_modules.calculator_module.operation import Operation


class BinaryOperation(Operation):
    @abc.abstractmethod
    def calculate_two(self, arg1, arg2):
        pass

    def calculate(self, *args):
        result = args[0]
        skipped_first = False
        for arg in args:
            if not skipped_first:
                skipped_first = True
                continue
            result = self.calculate_two(result,arg)
        return result

