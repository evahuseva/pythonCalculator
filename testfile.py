from main import calculator
from main import incoming_data
from random import randint
import unittest
import operator
import re


class MyTestCase(unittest.TestCase):

    def test_valid_input(self):
        self.data = '1*10-50000+200'
        self.valids = re.search('^(?:0|[1-9]\d*)(?:[+*-](?:0|[1-9]\d*))*$', self.data)
        self.result = calculator(self.data)
        self.assertEqual(self.result, -49790)

    def test_valid_input_error(self):
        self.valids = not re.search('^(?:0|[1-9]\d*)(?:[+*-](?:0|[1-9]\d*))*$', self.data) is None
        self.assertRaises(SyntaxError)
        assert 'Invalid input'

    def test_add(self):
        self.data = '1+2+3'
        self.result = calculator(self.data)
        self.assertEqual(self.result, 6)

    def test_add_error(self):
        self.data = '1+2+3'
        self.result = calculator(self.data)
        self.assertEqual(self.result, 0)

    def test_subtract(self):
        self.data = '1-2-3'
        self.result = calculator(self.data)
        self.assertEqual(self.result, -5)

    def test_subtract_error(self):
        self.data = '1-2-3'
        self.result = calculator(self.data)
        self.assertEqual(self.result, 0)

    def test_multipy(self):
        self.data = '1*2*3*4*5*6*7-8*9*10*11'
        self.result = calculator(self.data)
        self.assertEqual(self.result, -2880)

    def test_multipy_error(self):
        self.data = '1*2*3*4*5*6*7-8*9*10*11'
        self.result = calculator(self.data)
        self.assertEqual(self.result, 0)


if __name__ == '__main__':
    unittest.main()
