import unittest

import main.duplicate_chars as t

class TestDuplicateChars(unittest.TestCase):

    def test_check_for_duplicate_chars_with_duplicates(self):
        self.assertIsNotNone(t.check_for_duplicate_chars("aa"))
        self.assertIsNotNone(t.check_for_duplicate_chars("beep"))
        self.assertEqual(True, t.check_for_duplicate_chars("beep"))
        self.assertEqual(True, t.check_for_duplicate_chars("How have you been?"))

    def test_check_for_duplicate_chars_without_duplicate(self):
        self.assertIsNotNone(t.check_for_duplicate_chars("a"))
        self.assertEqual(False, t.check_for_duplicate_chars("bop"))
        self.assertEqual(False, t.check_for_duplicate_chars("asdfghjp"))
