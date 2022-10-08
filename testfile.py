from main import Calc
import main
import unittest
import re


class MyTestCase(unittest.TestCase):

    def test_string_input(self):
        self.get_expression = main.expression
        try:
            if type(self.get_expression) != str:
                raise TypeError
        except TypeError:
            return 'Type error occurred.'

    def test_valid_input(self):
        self.get_expression = main.expression
        self.isvalid = not re.search('^(?:0|[1-9]\d*)(?:[+*-](?:0|[1-9]\d*))*$', main.expression) is None
        try:
            if self.isvalid:
                pass
        except SyntaxError:
            return 'Syntax error occurred.'

    def test_calculation(self):
        main.expression = '1*10-50000+200'
        example = Calc()
        self.call_calculating = str(example.calculating())
        if self.assertEqual(self.call_calculating, '-49790'):
            pass
        else:
            assert 'Unsolved calculation problem.'

    def test_zero_division(self):
        example = Calc()
        try:
            example.calculating()
        except ZeroDivisionError:
            print('Zero Division')


if __name__ == '__main__':
    unittest.main()
    
