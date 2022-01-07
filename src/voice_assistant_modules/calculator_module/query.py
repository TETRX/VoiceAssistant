import portion as P

from src.voice_assistant_modules.calculator_module.operations.binary_operations.addition_operation import \
    AdditionOperation
from src.voice_assistant_modules.calculator_module.operations.binary_operations.division_operation import \
    DivisionOperation
from src.voice_assistant_modules.calculator_module.operations.binary_operations.minus_binary_operation import Minus
from src.voice_assistant_modules.calculator_module.operations.number_parsing_operation import NumberParsingOperation
from src.voice_assistant_modules.calculator_module.operations.unary_operations.trigonometric_operations.sine_operation import SineOperation
from src.voice_assistant_modules.calculator_module.operations.unary_operations.trigonometric_operations.tangent_operation import TangentOperation


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

    def calculate(self, start=0, end=None, curr_priority_index=0):
        if end is None:
            end = len(self.text)

        relevant_interval = P.open(start, end)
        relevant_operations_in_text = self.operations_in_text[relevant_interval]

        while curr_priority_index != len(self.operations_in_order_of_execution)-1:
            curr_prioritized_operations = self.operations_in_order_of_execution[curr_priority_index]
            curr_operations_in_text = P.Interval()
            for operation in curr_prioritized_operations:
                curr_operations_in_text |= relevant_operations_in_text.find(operation)
            if not curr_operations_in_text.empty:
                curr_operation_in_text = list(curr_operations_in_text)[0]  # get the first instance of an operation in the text, from the right
                curr_prioritized_operation = self.operations_in_text[curr_operation_in_text].values()[0]  # get the operation object to execute
                # self.operations_in_text[curr_operation_in_text] is an IntervalDict, because curr_operation_in_text is an interval,
                # but it only ever contains one value, because of the logic of this program, thus we can safely just take the first one.
                args_in_text = (~curr_operation_in_text) & relevant_interval
                partial_results = [
                    self.calculate(start=int(interval.lower), end=int(interval.upper), curr_priority_index=curr_priority_index)
                    for interval in args_in_text]
                return curr_prioritized_operation().calculate(*partial_results)
            curr_priority_index += 1
        else:
            return self.operations_in_order_of_execution[-1][0]().calculate(self.text[start: end])


if __name__ == '__main__':
    query = Query("123 plus 533", [(AdditionOperation,), (NumberParsingOperation,)],
                  [AdditionOperation, NumberParsingOperation])
    query.parse()
    print(query.calculate())

    query2 = Query("123 podzielone przez minus 15", [(Minus.minus(DivisionOperation),), (DivisionOperation,), (NumberParsingOperation,)], [Minus.minus(DivisionOperation), DivisionOperation, NumberParsingOperation])
    query2.parse()
    print(query2.calculate())

    query3 = Query("sinus z p", [(SineOperation,), (NumberParsingOperation,)], [SineOperation, NumberParsingOperation])
    query3.parse()
    print(query3.calculate())

    query4 = Query("sinus z sinusa z p", [(SineOperation,), (NumberParsingOperation,)], [SineOperation, NumberParsingOperation])
    query4.parse()
    print(query4.calculate())

    query5 = Query("sinus z tangensa z p/4", [(SineOperation, TangentOperation), (NumberParsingOperation,)], [SineOperation, TangentOperation, NumberParsingOperation])
    query5.parse()
    print(query5.calculate())

    query6 = Query("tangens z sinusa z p/4", [(SineOperation, TangentOperation), (NumberParsingOperation,)], [SineOperation, TangentOperation, NumberParsingOperation])
    query6.parse()
    print(query6.calculate())