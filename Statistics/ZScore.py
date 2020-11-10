from Statistics.Standard_Deviation import sample_standard_deviation, standard_deviation
from Statistics.Validation import is_valid
from Statistics.Mean import mean
from Calculator.Subtraction import subtraction as subtract
from Calculator.Division import division as divide


def z_score_list(data):
    if is_valid(data):
        tmp = []
        u = mean(data)
        s = standard_deviation(data)
        for x in data:
            tmp.append(z_score(x, u, s))
        return tmp
    else:
        raise TypeError("Data contains non-numeric values")


def z_score(x, u, s):
    var_1 = subtract(x, u)
    return divide(var_1, s)
