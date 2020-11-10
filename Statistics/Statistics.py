from Calculator.Calculator import Calculator
from Statistics.Standard_Deviation import standard_deviation, sample_standard_deviation

from Statistics.Variance import s_variance
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Variance import variance

from Statistics.Validation import is_valid
from Statistics.Sampling import seed_select_sample, conf_inter, mar_err, cochran, sample_size_ci
from Statistics.ZScore import z_score_list, z_score


class Statistics(Calculator):

    def mean(self, data):
        if is_valid(data):
            self.result = mean(data)
            return self.result
        else:
            raise TypeError("Data contains non-numeric values")

    def median(self, data):
        if is_valid(data):
            self.result = median(data)
            return self.result
        else:
            raise TypeError("Data contains non-numeric values")

    def mode(self, data):
        if is_valid(data):
            self.result = mode(data)
            return self.result
        else:
            raise TypeError("Data contains non-numeric values")

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def sample_variance(self, data):
        self.result = s_variance(data)
        return self.result

    def standard_deviation(self, data):
        self.result = standard_deviation(data)
        return self.result

    def sample_standard_deviation(self, data):
        self.result = sample_standard_deviation(data)
        return self.result

    def z_score_list(self, data):
        self.result = z_score_list(data)
        return self.result

    def z_score(self, x, u, s):
        self.result = z_score(x,u,s)
        return self.result

    def simple_random_sample(self, data, size):
        return seed_select_sample(data, size)

    def confidence_interval(self, x, cl, s, n):
        self.result = conf_inter(x, cl, s, n)
        return self.result

    def margin_of_err(self, z, s, n):
        self.result = mar_err(z, s, n)
        return self.result

    def cochran(self, z, p, q, e):
        self.result = cochran(z, p, q, e)
        return self.result

    def sample_size_ci(self, z, p, w):
        self.result = sample_size_ci(z, p, w)
        return self.result
