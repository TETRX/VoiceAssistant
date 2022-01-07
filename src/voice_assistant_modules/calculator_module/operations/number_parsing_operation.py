from src.voice_assistant_modules.calculator_module.operation import Operation
from fractions import Fraction
from math import pi, e
import re


class NoNumberToParseException(Exception):
    pass


class NumberParsingOperation(Operation):
    """
    A unit will be anything at the end of the number signifying that the previous part is a number relating to the
    quantity of the unit. For example: "milionów" ("millions") in the phrase "pięć milionów" ("five millions") or
    "piąte" ("fifths") in the phrase "trzy piąte" ("three fifths").
    This also includes things like "000" in "200 000" (what STT outputs for "dwieście tysięcy" ("two hundred thousand")).
    These are not units in the sense of measures of some properties - kilograms or meters, these are beyond the scope of
    this module.
    """
    BIGNUMBER_UNITS = {
        "milionów": 1000000,
        "miliardów": 1000000000,
        "bilionów": 10 ** 12,
        "biliardów": 10 ** 15,
        "trylionów": 10 ** 18,
        "tryliardów": 10 ** 21,
        "kwadrylionów": 10 ** 24,
        "kwadryliardów": 10 ** 27
    }

    FRACTION_NL_UNITS = {
        "drugich": Fraction(1, 2),
        "trzecich": Fraction(1, 3),
        "czwartych": Fraction(1, 4),
        "piątych": Fraction(1, 5),
        "szóstych": Fraction(1, 6),
        "siódmych": Fraction(1, 7),
        "ósmych": Fraction(1, 8),
        "dziewiątych": Fraction(1, 9),
        "dziesiątych": Fraction(1, 10),
        "setnych": Fraction(1, 100)
    }
    FRACTION_NL_UNITS_IN_DIFFERENT_FORMS = {}
    for fraction_nl_unit in FRACTION_NL_UNITS:
        FRACTION_NL_UNITS_IN_DIFFERENT_FORMS[fraction_nl_unit.replace("ich","e")] = FRACTION_NL_UNITS[fraction_nl_unit]
        FRACTION_NL_UNITS_IN_DIFFERENT_FORMS[fraction_nl_unit.replace("ych","e")] = FRACTION_NL_UNITS[fraction_nl_unit]
    FRACTION_NL_UNITS=dict(FRACTION_NL_UNITS,**FRACTION_NL_UNITS_IN_DIFFERENT_FORMS)


    for big_num in BIGNUMBER_UNITS:
        FRACTION_NL_UNITS[big_num.replace("ów", "owych")] = Fraction(1, BIGNUMBER_UNITS[big_num])

    OTHER_UNITS = {
        " 000": 1000,
        "p": pi,
        "E": e
    }

    HARDCODED_UNITS = dict(dict(BIGNUMBER_UNITS, **FRACTION_NL_UNITS), **OTHER_UNITS)

    FRACTION_PROCESSED_UNITS = r'/[0-9]+$'

    def _handle_units(self, number_as_string: str):
        last_iteration_failed = False
        multiplier = 1
        while not last_iteration_failed:
            last_iteration_failed = True
            for unit in NumberParsingOperation.HARDCODED_UNITS:
                if number_as_string.endswith(unit):
                    multiplier *= NumberParsingOperation.HARDCODED_UNITS[unit]
                    number_as_string = number_as_string[:-len(unit)]
                    last_iteration_failed = False

            search_processed_fraction = re.search(NumberParsingOperation.FRACTION_PROCESSED_UNITS, number_as_string)
            if search_processed_fraction is not None:
                processed_fraction = search_processed_fraction.group(0)
                multiplier *= Fraction(1, int(processed_fraction[-1:]))
                number_as_string = number_as_string[:-len(processed_fraction)]
                last_iteration_failed = False
        return multiplier, number_as_string

    # luckily, most of the numbers are automatically converted to numerics by stt, so we need to only handle some of
    # them.
    SINGLE_NUMBER_DICTIONARY = {
        "": 1,
        "jeden": 1,
        "jednego": 1,
        "dwa": 2,
        "dwóch": 2,
        "trzy": 3,
        "trzech": 3,
        "cztery": 4,
        "czterech": 4,
        "pięć": 5,
        "pięciu": 5,
        "sześć": 6,
        "sześciu": 6,
        "siedem": 7,
        "siedmiu": 7,
        "osiem": 8,
        "ośmiu": 8,
        "dziewięć": 9,
        "dziewięciu": 9,
        "dziesięć": 10,
        "dziesięciu": 10,
        "sto": 100,
        "dwieście": 200,
        "dwustu": 200,
        "trzysta": 300,
        "trzystu": 300,
        "czterysta": 400,
        "czterystu": 400,
        "pięćset": 500,
        "pięciuset": 500,
        "sześćset": 600,
        "sześciuset": 600,
        "siedemset": 700,
        "siedmiuset": 700,
        "osiemset": 800,
        "ośmiuset": 800,
        "dziewięćset": 900,
        "dziewięciuset": 900
    }

    for unit in BIGNUMBER_UNITS:
        SINGLE_NUMBER_DICTIONARY[unit.replace("ów", "")] = BIGNUMBER_UNITS[unit]
        SINGLE_NUMBER_DICTIONARY[unit.replace("ów", "a")] = BIGNUMBER_UNITS[unit]

    def _parse_single_number(self, number):
        try:
            return int(number)
        except:
            return NumberParsingOperation.SINGLE_NUMBER_DICTIONARY[number.replace(" ", "")]

    @classmethod
    def get_keywords(cls):
        return []

    def calculate(self, *args):
        try:
            return self.parse(args[0])
        except IndexError:
            raise NoNumberToParseException

    def parse(self, text):
        if text.replace(" ", "") == "":  # return None if string is effectively empty. We don't want to throw an
            # exception because sometimes we will just never use this. This way it will only throw an exception if it
            # is actually used.
            return None
        multiplier, single_number = self._handle_units(text)
        return multiplier*self._parse_single_number(single_number)


