import unittest

import main.linked_list as t

class TestNode(unittest.TestCase):

    def test_init(self):
        self.assertIsNotNone(t.Node(1))
        self.assertIsNotNone(t.Node(1, n=2))
    
    def test_get_data(self):
        node = t.Node(1, n=2)
        self.assertEqual(1, node.get_data())

    def test_set_data(self):
        node = t.Node(1, n=2)
        self.assertEqual(1, node.get_data())
        node.set_data(3)
        self.assertEqual(3, node.get_data())

    def test_get_next(self):
        node = t.Node(9, n=10)
        self.assertEqual(10, node.get_next())

    def test_set_next(self):
        node = t.Node(1,n=3)
        self.assertEqual(3, node.get_next())
        node.set_next(11)
        self.assertEqual(11, node.get_next())
