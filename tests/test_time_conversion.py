import unittest
import main.time_conversion as t

class TestTimeConversion(unittest.TestCase):

    def test_time_conversion_with_none(self):
        self.assertEqual(None, t.timeConversion(None))


    def test_time_conversion_with_empty(self):
        self.assertEqual(None, t.timeConversion({}))
        self.assertEqual(None, t.timeConversion([]))


    def test_time_conversion(self):
        self.assertIsNotNone(t.timeConversion("5:00:00PM"))
        self.assertEqual("17:00:00", t.timeConversion("5:00:00PM"))
        self.assertEqual("05:00:00", t.timeConversion("5:00:00AM"))
    

    def test_time_conversion_noon(self):
        self.assertIsNotNone(t.timeConversion("12:00:00PM"))
        self.assertEqual("12:00:00", t.timeConversion("12:00:00PM"))


    def test_time_conversion_midnight(self):
        self.assertIsNotNone(t.timeConversion("12:00:00AM"))
        self.assertEqual("00:00:00", t.timeConversion("12:00:00AM"))
