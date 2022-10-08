from main import Calc
import main
import unittest
import re


class MyTestCase(unittest.TestCase):

    def test_invalid_type_input(self):
        self.input_type = type(main.expression)
        self.assertEqual(self.input_type, str)

    def test_valid_input(self):
        self.isvalid = not re.search('^(?:0|[1-9]\d*)(?:[+*-](?:0|[1-9]\d*))*$', main.expression) is None
        self.assertEqual(self.isvalid, True)

    def test_calculation(self):
        example = Calc()
        main.expression = '1*10-50000+200'
        self.call_calculating = str(example.calculating())
        self.assertEqual(self.call_calculating, '-49790')

    def test_zero_division(self):
        self.is_zero_division = False
        if '/0' in main.expression:
            self.is_zero_division = True
        self.assertEqual(self.is_zero_division, False)


if __name__ == '__main__':
    unittest.main()
