import unittest

import main.reverse_integer as t

class TestReverseInteger(unittest.TestCase):
    
    def test_reverse_integer_not_none(self):
        self.assertIsNotNone(t.reverse_integer(123))

    def test_reverse_integer_is_num(self):
        self.assertEqual(int, type(t.reverse_integer(123)))
        self.assertEqual(None, t.reverse_integer("123"))
        self.assertEqual(None, t.reverse_integer(None))

    def test_reverse_integer_is_reversed(self):
        self.assertEqual(321, t.reverse_integer(123))
        self.assertEqual(111, t.reverse_integer(111))
        self.assertEqual(22446688, t.reverse_integer(88664422))
