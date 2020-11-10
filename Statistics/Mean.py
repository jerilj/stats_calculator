from Calculator.Addition import addition,add_list
from Calculator.Division import division


def mean(data):
    total = 0
    num = len(data)
    total = add_list(data)
    return division(total, num)
