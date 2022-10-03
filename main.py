def Numbers(num):
    return int(num)
#    return num == '0' or num == '1' or num == '2' or num == '3' or num == '4' or num == '5' or num == '6' or num == '7' or num == '8' or num == '9'


def Test4Num(varstr):
    null = 0
    var = ''
    try:
        while Numbers(varstr[null]):
            var += varstr[null]
            null += 1
    except: pass
    return int(var), null


def operation(string, num1, num2):
    if string == '+':
        return num1 + num2
    if string == '-':
        return num1-num2
    if string == '*':
        return num1*num2
    if string == '/':
        return num1/num2
    if string == '^':
        return num1 ** num2


result = operation(op, number1, number2)
