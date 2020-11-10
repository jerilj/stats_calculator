from Calculator.Addition import add_list
from Statistics.Validation import is_valid
from Calculator.Division import division as divide
from Calculator.Subtraction import subtraction as subtract
from Calculator.Square import square
from Statistics.Mean import mean


def variance(data):
    if is_valid(data):
        size = len(data)
        x = mean(data)
        tmp = []
        for i in data:
            diff = subtract(i, x)
            tmp.append(square(diff))
        total = add_list(tmp)
        return divide(total, size)
    else:
        raise TypeError("Data contains non-numeric values")


def s_variance(data):
    if is_valid(data):
        size = len(data)
        n = subtract(size, 1)
        x = mean(data)
        tmp = []
        for i in data:
            diff = subtract(i, x)
            tmp.append(square(diff))
        total = add_list(tmp)
        return divide(total, n)
    else:
        raise TypeError("Data contains non-numeric values")
