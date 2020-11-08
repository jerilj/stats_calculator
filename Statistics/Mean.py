from Calculator.Addition import addition
from Calculator.Division import division


def mean(data):
    total = 0
    num = len(data)
    for i in data:
        total = addition(total, i)
    return division(total, num)
