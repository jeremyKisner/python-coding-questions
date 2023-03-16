import unittest

import main.pandas_analysis as t

class TestPandasAnalysis(unittest.TestCase):

    def test_load(self):
        self.assertIsNotNone(t.load())
