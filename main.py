import re


def calculator(exp):
    pattern = "[a-zA-Z]+"
    if re.search(pattern, exp):
        return "Invalid input! No characters allowed."
    else:
        return eval(exp)


expression = input("Enter the expression: ")
print(calculator(expression))

# r1 = re.findall(r"^\w+",expression)
# print(r1)
