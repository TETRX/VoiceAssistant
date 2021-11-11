import abc
from collections import deque


class Operation:
    @classmethod
    @abc.abstractmethod
    def get_keywords(cls):
        pass

    @abc.abstractmethod
    def calculate(self, *args):
        pass

    @staticmethod
    def build_tree_and_calculate(operations, text):
        if len(operations) == 1:
            return operations[0].calculate(text)

        current_operation = operations[0]
        split_text = [text]
        for keyword in current_operation.get_keywords():
            new_split_text = []
            list_of_lists = [text_chunk.split(keyword) for text_chunk in split_text]

            for list_ in list_of_lists:
                new_split_text += list_

            split_text = new_split_text

        next_operations = operations[1:]
        if split_text[0] == text:  # no keywords of that operation_type - we can go straight to the next iteration
            return Operation.build_tree_and_calculate(next_operations, text)

        result = operations[0].calculate(*[Operation.build_tree_and_calculate(next_operations, text_chunk) for
                                               text_chunk in split_text])
        return result
