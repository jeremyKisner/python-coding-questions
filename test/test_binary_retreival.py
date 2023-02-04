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