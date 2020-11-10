import unittest
from CSVReader.TableReader import TableReader


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.table_reader = TableReader('csv/z-table.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.table_reader, TableReader)


if __name__ == '__main__':
    unittest.main()
