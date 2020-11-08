import unittest

from CSVReader.CSVReader import CSVReader
from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method(self):
        add_data = CSVReader('csv/Unit Test Addition.csv')
        for row in add_data.data:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))

    def test_subtract_method(self):
        sub_data = CSVReader('csv/Unit Test Subtraction.csv')
        for row in sub_data.data:
            self.assertEqual(self.calculator.subtract(int(row['Value 2']), int(row['Value 1'])), int(row['Result']))

    def test_multiply_method(self):
        sub_data = CSVReader('csv/Unit Test Multiplication.csv')
        for row in sub_data.data:
            self.assertEqual(self.calculator.multiply(int(row['Value 2']), int(row['Value 1'])), int(row['Result']))

    def test_divide_method(self):
        sub_data = CSVReader('csv/Unit Test Division.csv')
        for row in sub_data.data:
            self.assertEqual(round(self.calculator.divide(float(row['Value 2']), float(row['Value 1'])), 9),
                             float(row['Result']))

    def test_square_method(self):
        sub_data = CSVReader('csv/Unit Test Square.csv')
        for row in sub_data.data:
            self.assertEqual(self.calculator.square(int(row['Value 1'])), int(row['Result']))

    def test_sqrt_method(self):
        sub_data = CSVReader('csv/Unit Test Square Root.csv')
        for row in sub_data.data:
            self.assertEqual(round(self.calculator.square_root(float(row['Value 1'])), 8),
                             round(float(row['Result']), 8))


if __name__ == '__main__':
    unittest.main()
