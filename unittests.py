import unittest

from sll.sll import SLLNode
from sll.sll import SLL

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

    def test_SLL_add_top(self):
        sll = SLL()
        sll.add_top(0)
        sll.add_top(1)
        self.assertEqual(sll.head.get_data(), 1)
        self.assertEqual(sll.head.get_next().get_data(), 0)

    def test_SLL_add_bot(self):
        sll = SLL()
        sll.add_bot(0)
        sll.add_bot(1)
        self.assertEqual(sll.head.get_data(), 0)
        self.assertEqual(sll.head.get_next().get_data(), 1)

    def test_SLL_size(self):
        sll = SLL()
        self.assertEqual(sll.size(), 0)
        sll.add_top(0)
        self.assertEqual(sll.size(), 1)

    def test_SLL_contains(self):
        sll = SLL()
        self.assertTrue(not sll.contains(0))
        sll.add_top(0)
        self.assertTrue(sll.contains(0))

    def test_SLL_remove_top(self):
        sll = SLL()
        sll.add_top(0)
        sll.add_top(1)
        sll.add_top(2)
        node = sll.head
        sll.remove(node)
        self.assertEqual(sll.head.get_data(), 1)
        self.assertEqual(sll.size(), 2)

    def test_SLL_remove_mid(self):
        sll = SLL()
        sll.add_top(0)
        sll.add_top(1)
        sll.add_top(2)
        node = sll.head.get_next()
        sll.remove(node)
        self.assertEqual(sll.head.get_data(), 2)
        self.assertEqual(sll.head.get_next().get_data(), 0)
        self.assertEqual(sll.size(), 2)

    def test_SLL_remove_mid(self):
        sll = SLL()
        sll.add_top(0)
        sll.add_top(1)
        sll.add_top(2)
        node = sll.head.get_next().get_next()
        sll.remove(node)
        self.assertEqual(sll.head.get_data(), 2)
        self.assertEqual(sll.head.get_next().get_data(), 1)
        self.assertEqual(sll.size(), 2)

if __name__ == '__main__':
    unittest.main()
