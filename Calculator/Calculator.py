from Calculator.Addition import addition
from Calculator.Multiplication import multiplicaton
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from Calculator.SquareRoot import get_square_root


class Calculator:
    def __init__(self):
        self.result = 0
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplicaton(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = multiplicaton(a, a)
        return self.result

    def square_root(self, a):
        self.result = get_square_root(a)
        return self.result
