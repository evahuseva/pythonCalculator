class Calc:

    def __init__(self):
        self.result = None

    def calculating(self):
        try:
            for index in range(len(expression) - 1):
                if expression[index] in '*-+' and expression[index + 1] == expression[index]:
                    print('Repeating operators in a row.')
                    pass
            self.result = eval(str(expression))
            print(self.result)
        except ZeroDivisionError:
            print('Division by zero error.')
            pass
        except SyntaxError:
            print('Invalid expression input.')
            pass
        except TypeError:
            print('Invalid type input.')
            pass
        except NameError:
            print('Invalid input.')
            pass
        finally:
            pass


expression = input("Enter the expression: ")
c1 = Calc()
c1.calculating()
