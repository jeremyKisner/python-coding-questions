import unittest

import main.string_disorder as t

class TestStringDisorder(unittest.TestCase):

    def test_disorder(self):
        self.assertEqual("", t.disorder(None))
        self.assertIsNotNone(t.disorder("This is a sentence."))
        self.assertEqual(str, type(t.disorder(" test this string ")))
