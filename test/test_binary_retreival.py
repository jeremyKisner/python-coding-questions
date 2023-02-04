import unittest
import main.binary_retrieval as t

class TestBinaryRetrieval(unittest.TestCase):

    def test_binary_retreival(self):
        self.assertIsNone(t.binary_retrieval([1], 2))
        self.assertEqual(
            t.binary_retrieval(
                [1,1,1,1,1,1,2,2,3,3,3],
                1
            ),
            [1,1,1,1,1,1]
        )
        self.assertEqual(
            t.binary_retrieval(
                [1,1],
                1
            ),
            [1,1]
        )
        self.assertEqual(
            t.binary_retrieval(
                [1,2,2],
                2
            ),
            [2,2]
        )
        self.assertEqual(
            t.binary_retrieval(
                [1,2,2,2,4,4,5,6,7,8,9,9,9,9,9,9,9],
                2
            ),
            [2,2,2]
        )