from src.voice_assistant_modules.calculator_module.operation import Operation
from src.voice_assistant_modules.calculator_module.operations.binary_operations.addition_operation import \
    AdditionOperation
from src.voice_assistant_modules.calculator_module.operations.binary_operations.division_operation import \
    DivisionOperation
from src.voice_assistant_modules.calculator_module.operations.binary_operations.minus_binary_operation import Minus
from src.voice_assistant_modules.calculator_module.operations.binary_operations.multiplication_operation import \
    MultiplicationOperation
from src.voice_assistant_modules.calculator_module.operations.binary_operations.subtraction_operation import \
    SubtractionOperation
from src.voice_assistant_modules.calculator_module.operations.number_parsing_operation import NumberParsingOperation
from src.voice_assistant_modules.calculator_module.query import Query
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

    OPERATIONS_IN_ORDER_OF_EXECUTION = (
        Minus.minus(SubtractionOperation),
        SubtractionOperation,
        Minus.minus(AdditionOperation),
        AdditionOperation,
        Minus.minus(MultiplicationOperation),
        MultiplicationOperation,
        Minus.minus(DivisionOperation),
        DivisionOperation,
        NumberParsingOperation
    )

    OPERATIONS_IN_ORDER_OF_PARSING = (
        Minus.minus(MultiplicationOperation),
        Minus.minus(DivisionOperation),
        Minus.minus(AdditionOperation),
        Minus.minus(SubtractionOperation),
        MultiplicationOperation,
        DivisionOperation,
        AdditionOperation,
        SubtractionOperation,
    )

    def __init__(self, operations_in_order_of_execution=OPERATIONS_IN_ORDER_OF_EXECUTION,
                 operations_in_order_of_parsing=OPERATIONS_IN_ORDER_OF_PARSING, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.operations_in_order_of_execution = operations_in_order_of_execution  # the reverse order in which
        # operations should be executed. Must end with an operation parsing the string
        self.operations_in_order_of_parsing = operations_in_order_of_parsing  # the order in which the operations should
        # be parsed. Searching the earlier operations in text will be done first, and in the text where those operations
        # are found no later keywords will be searched

    def normalize_query(self, query_text):
        return query_text.lower()

    def process_query(self, query_text: str) -> str:
        query_text = self.normalize_query(query_text)
        for question in CalculatorModule.CALCULATION_QUESTIONS:
            if query_text.startswith(question):
                query_text = query_text[len(question) + 1:]  # now that we know it's a calculation question we can get
                # rid of the question part.
                break
        else:
            return None  # if not a calculation question, we can't answer it
        query_text = "0 plus " + query_text  # A bit of a trick - the value of any expression x is the same as the value of
        # 0 + x, but this way we get to handle the unary minus operator in a more general manner
        query = Query(query_text, self.operations_in_order_of_execution, self.operations_in_order_of_parsing)
        query.parse()
        return str(query.calculate())


if __name__ == '__main__':
    CalculatorModule.main()
    # calculator_module = CalculatorModule()
    # print(calculator_module.process_query("Ile jest 133 plus 832 podzielone przez 4"))