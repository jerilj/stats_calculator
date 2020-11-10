import random

from Calculator.Square import square
from Calculator.SquareRoot import get_square_root
from Statistics.Scores import get_t_score, get_z_score
from Calculator.Subtraction import subtraction as subtract
from Calculator.Division import division as divide
from Calculator.Multiplication import multiplicaton as multiply
from Calculator.Addition import addition as add


def seed_select_sample(data, n):
    random.seed(5)
    return random.sample(data, n)


def conf_inter(x, cl, s, n):
    var_1 = n - 1
    var_2 = subtract(1, cl)
    var_3 = divide(var_2, 2)
    var_4 = get_t_score(float(var_1), float(var_3))
    var_5 = get_square_root(n)
    var_6 = divide(s, var_5)
    var_7 = multiply(float(var_4), var_6)
    low = subtract(x, var_7)
    high = add(x, var_7)
    return [low, high]


def mar_err(z, s, n):
    var_1 = get_square_root(n)
    var_2 = divide(s, var_1)
    return multiply(z, var_2)


def cochran(z, p, q, e):
    var_1 = square(z)
    var_2 = multiply(p, q)
    var_3 = multiply(var_1, var_2)
    var_4 = square(e)
    return divide(var_3, var_4)


def sample_size_ci(z, p, w):
    var_1 = divide(z, 2)
    z_score = get_z_score(var_1)
    e = divide(w, 2)
    q = subtract(1, p)
    var_2 = multiply(p, q)
    var_3 = divide(float(z_score), e)
    var_5 = square(var_3)
    return multiply(var_2, var_5)
