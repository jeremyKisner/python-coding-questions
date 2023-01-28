import unittest
import main.multithreaded_addition as t

class TestMultiThreadAddition(unittest.TestCase):

    def test_add(self):
        self.assertEqual(2, t.add(1,1))
        self.assertEqual(0, t.add(0,0))
        self.assertEqual(1, t.add(0,1))
        self.assertEqual(-1, t.add(0,-1))
        self.assertEqual(2, t.add(3,-1))

    def test_process(self):
        list1 = [1,2,3,4,5,6,7,8,9,10]
        list2 = list1[::-1]
        self.assertNotEqual(None, t.process(list1, list2))
