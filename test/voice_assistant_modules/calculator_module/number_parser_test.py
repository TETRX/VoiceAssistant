import unittest
import json

from src.utils.paths import get_root_dir, get_test_path
from src.voice_assistant_modules.calculator_module.operations.number_parsing_operation import NumberParsingOperation
from os import path

from test.test_generator import TestGenerator


class NumberParserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.filepath = path.join(get_test_path(), TestGenerator.TESTCASES_DIR, "voice_assistant_modules/calculator_module/numbers.json")

    def test_json_testcases(self):
        with open(self.filepath, "r") as file:
            testcases = json.load(file)

        number_parser = NumberParsingOperation()
        for testcase in testcases:
            print(testcase)
            self.assertAlmostEqual(testcase["expected_answer"],number_parser.parse(testcase["phrase"]))


if __name__ == '__main__':
    unittest.main()
