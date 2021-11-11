from src.voice_assistant_modules.calculator_module.operation import Operation
from src.voice_assistant_modules.calculator_module.operations.binary_operations.addition_operation import \
    AdditionOperation
from src.voice_assistant_modules.calculator_module.operations.binary_operations.division_operation import \
    DivisionOperation
from src.voice_assistant_modules.calculator_module.operations.binary_operations.minus_binary_operation import minus
from src.voice_assistant_modules.calculator_module.operations.binary_operations.multiplication_operation import \
    MultiplicationOperation
from src.voice_assistant_modules.calculator_module.operations.binary_operations.subtraction_operation import \
    SubtractionOperation
from src.voice_assistant_modules.calculator_module.operations.number_parsing_operation import NumberParsingOperation
from src.voice_assistant_modules.va_module import VAModule


class CalculatorModule(VAModule):
    CALCULATION_QUESTIONS = (
        "ile jest",
        "ile wynosi",
        "policz",
        "oblicz",
        "wylicz",
        "licz",
        "przelicz"
    )

    OPERATIONS = (
        SubtractionOperation,
        AdditionOperation,
        MultiplicationOperation,
        DivisionOperation,
        NumberParsingOperation
    )

    def __init__(self, operations=OPERATIONS, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operations = operations  # list of classes in order of execution, if order of execution is the same, in order in
        # which they should be found in text.

    def normalize_query(self, query):
        return query.lower()

    def process_query(self, query: str) -> str:
        query = self.normalize_query(query)
        for question in CalculatorModule.CALCULATION_QUESTIONS:
            if query.startswith(question):
                query = query[len(question)+1:]  # now that we know it's a calculation question we can get rid of the
                # question part.
                break
        else:
            return None  # if not a calculation question, we can't answer it
        # query = "zero plus " + query  # A bit of a trick - the value of any expression x is the same as the value of
        # 0 + x, but this way we get to handle the unary minus operator in a more general manner

        return Operation.build_tree_and_calculate([operation() for operation in self.operations],query)





if __name__ == '__main__':
    calculator_module = CalculatorModule()
    print(calculator_module.process_query("Ile jest 4 razy 2"))