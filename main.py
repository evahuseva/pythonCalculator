import re


def calculator(exp):
    pattern = "[a-zA-Z]+"
    if re.search(pattern, exp):
        return "Invalid input! No characters allowed."
    else:
        return eval(exp)


def incoming_data(*args):
    expression = input("Enter the expression: ")
    return expression


if __name__ == '__main__':
    print(calculator(incoming_data()))

# r1 = re.findall(r"^\w+",expression)
# print(r1)
