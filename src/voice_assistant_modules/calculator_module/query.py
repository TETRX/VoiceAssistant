import portion as P

from src.voice_assistant_modules.calculator_module.operations.binary_operations.addition_operation import \
    AdditionOperation
from src.voice_assistant_modules.calculator_module.operations.binary_operations.division_operation import \
    DivisionOperation
from src.voice_assistant_modules.calculator_module.operations.binary_operations.minus_binary_operation import Minus
from src.voice_assistant_modules.calculator_module.operations.number_parsing_operation import NumberParsingOperation


class Query:
    def __init__(self, text, operations_in_order_of_execution, operations_in_order_of_parsing):
        self.text = text
        self.operations_in_order_of_execution = operations_in_order_of_execution
        self.operations_in_order_of_parsing = operations_in_order_of_parsing
        self.operations_in_text = P.IntervalDict()

    def parse(self):
        for operation in self.operations_in_order_of_parsing:
            for interval in operation.get_keywords_in_text(self.text):
                if interval not in self.operations_in_text:
                    self.operations_in_text[interval] = operation

    def calculate(self, start=0, end=None, curr_operation_index=0):
        if end is None:
            end = len(self.text)

        relevant_interval = P.open(start, end)
        relevant_operations_in_text = self.operations_in_text[relevant_interval]

        while curr_operation_index != len(self.operations_in_order_of_execution)-1:
            curr_operation = self.operations_in_order_of_execution[curr_operation_index]
            curr_operation_in_text = relevant_operations_in_text.find(curr_operation)
            if not curr_operation_in_text.empty:
                args_in_text = (~curr_operation_in_text) & relevant_interval
                partial_results = [
                    self.calculate(start=int(interval.lower), end=int(interval.upper), curr_operation_index=curr_operation_index+1)
                    for interval in args_in_text]
                return curr_operation().calculate(*partial_results)
            curr_operation_index += 1
        else:
            return self.operations_in_order_of_execution[-1]().calculate(self.text[start: end])


if __name__ == '__main__':
    query = Query("123 plus 533", [AdditionOperation, NumberParsingOperation],
                  [AdditionOperation, NumberParsingOperation])
    query.parse()
    print(query.calculate())

    query2 = Query("123 podzielone przez minus 15", [Minus.minus(DivisionOperation), DivisionOperation, NumberParsingOperation], [Minus.minus(DivisionOperation), DivisionOperation, NumberParsingOperation])
    query2.parse()
    print(query2.calculate())
