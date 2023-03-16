import unittest
import main.runner_up as t

class TestRunnerUp(unittest.TestCase):

    def test_runner_up_with_none(self):
        self.assertIsNone(t.runner_up(None))


    def test_runner_up_with_empty(self):
        self.assertIsNone(t.runner_up([]))
        self.assertIsNone(t.runner_up({}))


    def test_runner_up_with_one_score(self):
        self.assertIsNotNone(t.runner_up([1]))
        self.assertEqual(1, t.runner_up([1]))


    def test_runner_up(self):
        self.assertEqual(1, t.runner_up([1, 2]))
        self.assertEqual(1, t.runner_up([2, 1]))
        self.assertEqual(2, t.runner_up([2, 3, 1]))
        self.assertEqual(4, t.runner_up([4, 2, 3, 5, 1]))


    def test_runner_up_with_negatives(self):
        self.assertEqual(-1, t.runner_up([-3, -2, -1, 2]))
        self.assertEqual(-1, t.runner_up([1, -1, -2, -1]))
        self.assertEqual(-7, t.runner_up([-7, -7, -7, -7, -6]))
        self.assertEqual(-57, t.runner_up([57, 57, -57, 57]))
        self.assertEqual(0, t.runner_up([-10, 0, 10]))
