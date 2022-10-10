import re


class Calc:

    def __init__(self, input_expression):
        self.is_valid = False
        self.result = None
        self.expression = input_expression

    def validate(self):
        if not isinstance(self.expression, str):
            raise TypeError
        self.is_valid = not re.search('^(?:0|[1-9]\\d*)(?:[+*-](?:0|[1-9]\\d*))*$', self.expression) is None
        if not self.is_valid:
            raise SyntaxError('Invalid input syntax.')

    def calculate(self):
        self.validate()
        return eval(self.expression)

    def output(self):
        try:
            return self.calculate()
        except SyntaxError as syntax_error:
            return syntax_error.msg
        except TypeError:
            return "Wrong input type."
        except Exception as error:
            return f'Abnormal exit: Unexpected error has occurred ({error.msg}).'
