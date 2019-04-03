import unittest

from sll.sll import SLLNode, SLL
from dll.dll import DLLNode, DLL
from stack.stack import Stack

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


class TestDLLMethods(unittest.TestCase):
    def test_DLLNode_get_data(self):
        node = DLLNode(0)
        self.assertEqual(node.get_data(), 0)

    def test_DLLNode_set_data(self):
        node = DLLNode(0)
        node.set_data(1)
        self.assertEqual(node.get_data(), 1)

    def test_DLLNode_get_next(self):
        node0 = DLLNode(0)
        node1 = DLLNode(1)
        node0.next = node1
        self.assertEqual(node0.get_next(), node1)

    def test_DLLNode_set_next(self):
        node0 = DLLNode(0)
        node1 = DLLNode(1)
        node0.set_next(node1)
        self.assertEqual(node0.get_next(), node1)

    def test_DLLNode_get_prev(self):
        node0 = DLLNode(0)
        node1 = DLLNode(1)
        node0.prev = node1
        self.assertEqual(node0.get_prev(), node1)

    def test_DLLNode_set_prev(self):
        node0 = DLLNode(0)
        node1 = DLLNode(1)
        node0.set_prev(node1)
        self.assertEqual(node0.get_prev(), node1)

    def test_DLL_add_top(self):
        dll = DLL()
        dll.add_top(0)
        dll.add_top(1)
        self.assertEqual(dll.head.get_data(), 1)
        self.assertEqual(dll.head.get_next().get_data(), 0)

    def test_DLL_add_bot(self):
        dll = DLL()
        dll.add_bot(0)
        dll.add_bot(1)
        self.assertEqual(dll.head.get_data(), 0)
        self.assertEqual(dll.head.get_next().get_data(), 1)

    def test_DLL_size(self):
        dll = DLL()
        self.assertEqual(dll.size(), 0)
        dll.add_top(0)
        self.assertEqual(dll.size(), 1)

    def test_DLL_contains(self):
        dll = DLL()
        self.assertTrue(not dll.contains(0))
        dll.add_top(0)
        self.assertTrue(dll.contains(0))

    def test_DLL_remove_top(self):
        dll = DLL()
        dll.add_top(0)
        dll.add_top(1)
        dll.add_top(2)
        node = dll.head
        dll.remove(node)
        self.assertEqual(dll.head.get_data(), 1)
        self.assertEqual(dll.size(), 2)

    def test_DLL_remove_mid(self):
        dll = DLL()
        dll.add_top(0)
        dll.add_top(1)
        dll.add_top(2)
        node = dll.head.get_next()
        dll.remove(node)
        self.assertEqual(dll.head.get_data(), 2)
        self.assertEqual(dll.head.get_next().get_data(), 0)
        self.assertEqual(dll.size(), 2)

    def test_DLL_remove_mid(self):
        dll = DLL()
        dll.add_top(0)
        dll.add_top(1)
        dll.add_top(2)
        node = dll.head.get_next().get_next()
        dll.remove(node)
        self.assertEqual(dll.head.get_data(), 2)
        self.assertEqual(dll.head.get_next().get_data(), 1)
        self.assertEqual(dll.size(), 2)


class TestStackMethods(unittest.TestCase):
    def test_push(self):
        s = Stack()
        s.push(0)
        s.push(1)
        self.assertEqual(s.items.head.get_data(), 1)
        self.assertEqual(s.items.head.get_next().get_data(), 0)

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(0)
        self.assertTrue(not s.is_empty())

    def test_depth(self):
        s = Stack()
        self.assertEqual(s.depth(), 0)
        s.push(0)
        self.assertEqual(s.depth(), 1)

    def test_pop(self):
        s = Stack()
        s.push(0)
        s.push(1)
        item1 = s.pop()
        self.assertEqual(item1, 1)
        self.assertEqual(s.depth(), 1)
        item0 = s.pop()
        self.assertEqual(item0, 0)
        self.assertEqual(s.depth(), 0)

    def test_pop_fail(self):
        s = Stack()
        with self.assertRaises(Exception):
            s.pop()

    def test_top(self):
        s = Stack()
        s.push(0)
        s.push(1)
        self.assertEqual(s.top(), 1)

    def test_top_fail(self):
        s = Stack()
        with self.assertRaises(Exception):
            s.top()



if __name__ == '__main__':
    unittest.main()
