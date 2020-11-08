from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Validation import is_valid


class Statistics(Calculator):

    def mean(self, data):
        if is_valid(data):
            self.result = mean(data)
            return self.result
        else:
            print("Data contains non-numeric values")

    def median(self, data):
        if is_valid(data):
            self.result = median(data)
            return self.result
        else:
            print("Data contains non-numeric values")

    def mode(self, data):
        if is_valid(data):
            self.result = mode(data)
            return self.result
        else:
            print("Data contains non-numeric values")