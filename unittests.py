import unittest

from sll.sll import SLLNode

class TestDataStructures(unittest.TestCase):
    def test_SLLNode_get_data(self):
        node = SLLNode(0)
        self.assertEqual(node.get_data(), 0)


if __name__ == '__main__':
    unittest.main()
