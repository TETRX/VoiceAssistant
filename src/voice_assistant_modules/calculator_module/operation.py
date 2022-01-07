import abc
import portion as P
import re

class Operation(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def get_keywords(cls):
        pass

    @classmethod
    def get_keywords_in_text(cls, text):
        occurences = P.empty()
        keywords = cls.get_keywords()
        for keyword in keywords:
            keyword_occurences = [P.open(occurrence.start(), occurrence.end()) for occurrence in re.finditer(keyword, text)]
            for occurrence in keyword_occurences:
                occurences |= occurrence
        return occurences

    @abc.abstractmethod
    def calculate(self, *args):
        pass
