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


if __name__ == '__main__':
    unittest.main()
