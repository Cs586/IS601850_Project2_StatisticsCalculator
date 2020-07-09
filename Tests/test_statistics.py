import unittest
import random
import numpy as np
from numpy.random import seed
from numpy.random import randint

from Statistics.ItemsWithSeed import items_with_seed
from Statistics.RandomItem import random_item
from Statistics.RandomNumberWithSeed import random_integer, random_float
from Statistics.RandomlySelectSame import randomly_same
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
import ast
import pprint




def items_Wout_seed():
    pass


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 10, 20)
        self.statistics = Statistics()
        self.x = 1

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_statistics(self):
        test_data_mean = CsvReader("Tests/Data/descriptive_stats.csv").data
        for row in test_data_mean:
            input_data = ast.literal_eval(row['input'])  # This converts string representation of list into list type
            self.assertEqual(round(self.statistics.mean(input_data), 2), round(float(row['mean']), 2))
            self.assertEqual(round(self.statistics.result, 2), round(float(row['mean']), 2))

    def test_median_statistics(self):
        test_data_median = CsvReader("Tests/Data/descriptive_stats.csv").data
        for row in test_data_median:
            input_data = ast.literal_eval(row['input'])
            self.assertEqual(round(self.statistics.median(input_data), 2), round(float(row['median']), 2))
            self.assertEqual(round(self.statistics.result, 2), round(float(row['median']), 2))

    def test_mode_statistics(self):
        test_data_mode = CsvReader("Tests/Data/descriptive_stats.csv").data
        for row in test_data_mode:
            input_data = ast.literal_eval(row['input'])
            mode_data = ast.literal_eval(row['mode'])
            self.assertEqual(self.statistics.mode(input_data), mode_data)
            self.assertEqual(self.statistics.result, mode_data)

    def test_variance_statistics(self):
        test_data_variance = CsvReader("Tests/Data/descriptive_stats.csv").data
        for row in test_data_variance:
            input_data = ast.literal_eval(row['input'])
            self.assertEqual(round(self.statistics.variance(input_data), 2), round(float(row['variance']), 2))
            self.assertEqual(round(self.statistics.result, 2), round(float(row['variance']), 2))

    def test_stddev_statistics(self):
        test_data_stddev = CsvReader("Tests/Data/descriptive_stats.csv").data
        for row in test_data_stddev:
            input_data = ast.literal_eval(row['input'])
            self.assertEqual(round(self.statistics.stddev(input_data), 2), round(float(row['standard_deviation']), 2))
            self.assertEqual(round(self.statistics.result, 2), round(float(row['standard_deviation']), 2))

    def test_zscore_statistics(self):
        test_data_zscore = CsvReader("Tests/Data/zscore.csv").data
        for row in test_data_zscore:
            input_data, x = ast.literal_eval(row['input']), ast.literal_eval(row['x'])
            self.assertEqual(round(self.statistics.zscore(input_data, x), 2), round(float(row['result']), 2))
            self.assertEqual(round(self.statistics.result, 2), round(float(row['result']), 2))


    def test_items_with_seed(self):
        nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        random.seed(5)
        number_list = random.sample(nlist, self)
        self.assertEqual(items_with_seed(), self)

    def test_items_Wout_seed(self):
        nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        number_list = random.sample(nlist, self)
        self.assertEqual(items_Wout_seed(), self)

    def test_randomly_same(self):
        nlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        random.seed(5)
        number_list = random.sample(nlist, self)
        self.assertEqual(randomly_same(1), self)

    def random_item(self):
        nList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result_numbered_list = random.sample(nList, 5)
        self.assertEqual(len(random_item(5)), len(result_numbered_list))

    def random_integer(self):
        nlist = (range(1, 10))
        random.seed(5)
        result_number_list = random.sample(nlist, 5)
        self.assertEqual(len(random_integer(5)), len(result_number_list))


    def random_float(self):
        nlist = (np.arange(1.0, 10.0))
        random.seed(5)
        result_ran_float = random.uniform(nlist, 5)
        self.assertEqual(len(random_float(5)), len(result_ran_float))











if __name__ == '__main__':
    unittest.main()
