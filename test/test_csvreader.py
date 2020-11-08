import unittest
from CSVReader.CSVReader import CSVReader


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.csv_reader = CSVReader('csv/Unit Test Addition.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.csv_reader, CSVReader)


if __name__ == '__main__':
    unittest.main()
