import unittest
import main.find_largest_num as t

class TestFindLargestNum(unittest.TestCase):

    def test_find_largest_num_none(self):
        self.assertIsNone(t.find_largest_num(None))

    def test_find_largest_num_not_num(self):
        self.assertIsNone(t.find_largest_num("how did i get here"))
        self.assertIsNone(t.find_largest_num(["w","o","o","p","s"]))

    def test_find_largest_num(self):
        self.assertIsNotNone(t.find_largest_num([1,9,4,7]))
        self.assertEqual(9, t.find_largest_num([1,9,4,7]))
        self.assertEqual(1, t.find_largest_num([1,1,1,1]))
        self.assertEqual(9, t.find_largest_num([1,9,4,7]))
        self.assertEqual(9, t.find_largest_num(["a",9,"10",7]))
