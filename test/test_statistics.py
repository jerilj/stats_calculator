import unittest
import random
import statistics as stats
import test.randoms as rand
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics()

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_method(self):
        random.seed(5)
        data = rand.seed_list_int(0, 10, 5)
        ans = stats.mean(data)
        self.assertEqual(self.statistics.mean(data), ans)

    def test_mean_method_dec(self):
        random.seed(5)
        data = rand.seed_list_dec(0, 10, 5)
        ans = stats.mean(data)
        self.assertEqual(self.statistics.mean(data), ans)

    def test_mean_method_empty(self):
        data = []
        with self.assertRaises(Exception):
            self.statistics.mean(data)

    def test_mean_method_str(self):
        data = [1, 2, "Hello World"]
        with self.assertRaises(TypeError):
            self.statistics.mean(data)

    def test_median_method_odd(self):
        random.seed(5)
        data = rand.seed_list_int(0, 10, 5)
        ans = stats.median(data)
        self.assertEqual(self.statistics.median(data), ans)

    def test_median_method_even(self):
        random.seed(5)
        data = rand.seed_list_dec(0, 10, 6)
        ans = stats.median(data)
        self.assertEqual(self.statistics.median(data), ans)

    def test_median_method_empty(self):
        data = []
        with self.assertRaises(Exception):
            self.statistics.median(data)

    def test_median_method_str(self):
        data = [1, 2, "Hello World"]
        with self.assertRaises(TypeError):
            self.statistics.median(data)

    def test_mode_method(self):
        random.seed(5)
        data = rand.seed_list_int(0, 10, 20)
        ans = stats.mode(data)
        self.assertEqual(self.statistics.mode(data), ans)

    def test_mode_method_empty(self):
        data = []
        with self.assertRaises(Exception):
            self.statistics.mode(data)

    def test_mode_method_str(self):
        data = [1, 2, "Hello World"]
        with self.assertRaises(TypeError):
            self.statistics.mode(data)

    def test_simple_sampling_method(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        size = 3
        ans = [5, 6, 7]
        self.assertEqual(self.statistics.simple_random_sample(data, size), ans)

    def test_confidence_interval_method(self):
        self.assertEqual(self.statistics.confidence_interval(240, 0.95, 25, 10), [222.1173198317478, 257.8826801682522])

    def test_margin_of_error_method(self):
        self.assertEqual(self.statistics.margin_of_err(1.645, 0.4, 900), 0.021933333333333336)

    def test_cochran_method(self):
        self.assertEqual(self.statistics.cochran(1.960, 0.5, 0.5, 0.05), 384.1599999999999)

    def test_sample_size_ci_method(self):
        self.assertEqual(self.statistics.sample_size_ci(0.95, 0.41, 0.06), 1032.536711111111)

    def test_variance_method(self):
        data = [600, 470, 170, 430, 300]
        ans = stats.variance(data)
        self.assertEqual(self.statistics.sample_variance(data), ans)

    def test_standard_deviation_method(self):
        data = [600, 470, 170, 430, 300]
        ans = stats.stdev(data)
        self.assertEqual(self.statistics.sample_standard_deviation(data), ans)

    def test_z_score_method(self):
        self.assertEqual(self.statistics.z_score(190, 150, 25), 1.6)

    def test_z_score_list_method(self):
        data = [0.7972, 0.0767, 0.4383]
        ans = [1.2232121397887195, -1.2262718699883022, 0.0030597301995827185]
        self.assertEqual(self.statistics.z_score_list(data), ans)


if __name__ == '__main__':
    unittest.main()
