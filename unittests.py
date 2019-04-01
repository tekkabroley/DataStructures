import unittest

from sll.sll import SLLNode

class TestSLLMethods(unittest.TestCase):
    def test_SLLNode_get_data(self):
        node = SLLNode(0)
        self.assertEqual(node.get_data(), 0)

    def test_SLLNode_set_data(self):
        node = SLLNode(0)
        node.set_data(1)
        self.assertEqual(node.get_data(), 1)

    def test_SLLNode_get_next(self):
        node0 = SLLNode(0)
        node1 = SLLNode(1)
        node0.next = node1
        self.assertEqual(node0.get_next(), node1)

    def test_SLLNode_set_next(self):
        node0 = SLLNode(0)
        node1 = SLLNode(1)
        node0.set_next(node1)
        self.assertEqual(node0.get_next(), node1)

if __name__ == '__main__':
    unittest.main()
