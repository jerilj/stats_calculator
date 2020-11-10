from Calculator.SquareRoot import get_square_root
from Statistics.Validation import is_valid
from Statistics.Variance import variance, s_variance


def standard_deviation(data):
    if is_valid(data):
        var = variance(data)
        return get_square_root(var)
    else:
        raise TypeError("Data contains non-numeric values")


def sample_standard_deviation(data):
    if is_valid(data):
        var = s_variance(data)
        return get_square_root(var)
    else:
        raise TypeError("Data contains non-numeric values")

