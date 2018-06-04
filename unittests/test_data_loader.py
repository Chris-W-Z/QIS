
# Author: Chris Zhu
# Created on: 03/07/2018
# Last Update: 03/07/2018

from loaders.data_loader import HistDataLoader
import unittest

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.loader = HistDataLoader()

    def test_load_0(self):
        self.assertEqual(self.loader.load(), 1)

if __name__ == '__main__':
    unittest.main()