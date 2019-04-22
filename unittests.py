import unittest

from sll.sll import SLLNode, SLL
from dll.dll import DLLNode, DLL
from stack.stack import Stack, EmptyStackException
from queue.queue import Queue, EmptyQueueException
from dequeue.dequeue import DEQueue, EmptyDEQueueException

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
        with self.assertRaises(EmptyStackException):
            s.pop()

    def test_top(self):
        s = Stack()
        s.push(0)
        s.push(1)
        self.assertEqual(s.top(), 1)

    def test_top_fail(self):
        s = Stack()
        with self.assertRaises(EmptyStackException):
            s.top()


class TestQueueMethods(unittest.TestCase):
    def test_length(self):
        q = Queue()
        self.assertEqual(q.length(), 0)
        q.items.add_top(0)
        self.assertEqual(q.length(), 1)

    def test_enqueue(self):
        q = Queue()
        q.enqueue(0)
        q.enqueue(1)
        item1 = q.items.head.get_data()
        item2 = q.items.head.get_next().get_data()
        self.assertEqual(item1, 0)
        self.assertEqual(item2, 1)

    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(0)
        self.assertTrue(not q.is_empty())

    def test_dequeue(self):
        q = Queue()
        q.enqueue(0)
        q.enqueue(1)
        item1 = q.dequeue()
        item2 = q.dequeue()
        self.assertEqual(item1, 0)
        self.assertEqual(item2, 1)
        self.assertTrue(q.is_empty())

    def test_dequeue_fail(self):
        q = Queue()
        with self.assertRaises(EmptyQueueException):
            q.dequeue()

    def test_front(self):
        q = Queue()
        q.enqueue(0)
        q.enqueue(1)
        item = q.front()
        self.assertEqual(item, 0)
        self.assertEqual(q.length(), 2)

    def test_front_fail(self):
        q = Queue()
        with self.assertRaises(EmptyQueueException):
            q.front()


class TestDEQueueMethods(unittest.TestCase):
    def test_length(self):
        dq = DEQueue()
        self.assertEqual(dq.length(), 0)
        dq.items.add_top(0)
        self.assertEqual(dq.length(), 1)

    def test_enqueue_front(self):
        dq = DEQueue()
        dq.enqueue_front(0)
        dq.enqueue_front(1)
        self.assertEqual(dq.length(), 2)
        head = dq.items.head
        self.assertEqual(head.get_data(), 1)
        self.assertEqual(head.get_next().get_data(), 0)

    def test_is_empty(self):
        dq = DEQueue()
        self.assertTrue(dq.is_empty())
        dq.enqueue_front(0)
        self.assertTrue(not dq.is_empty())

    def test_enqueue_back(self):
        dq = DEQueue()
        dq.enqueue_back(0)
        dq.enqueue_back(1)
        self.assertEqual(dq.length(), 2)
        head = dq.items.head
        self.assertEqual(head.get_data(), 0)
        self.assertEqual(head.get_next().get_data(), 1)

    def test_dequeue_front(self):
        dq = DEQueue()
        dq.enqueue_back(0)
        dq.enqueue_back(1)
        val1 = dq.dequeue_front()
        val2 = dq.dequeue_front()
        self.assertEqual(val1, 0)
        self.assertEqual(val2, 1)

    def test_dequeue_front_fail(self):
        dq = DEQueue()
        with self.assertRaises(EmptyDEQueueException):
            dq.dequeue_front()

    def test_dequeue_back(self):
        dq = DEQueue()
        dq.enqueue_back(0)
        dq.enqueue_back(1)
        val1 = dq.dequeue_back()
        val2 = dq.dequeue_back()
        self.assertEqual(val1, 1)
        self.assertEqual(val2, 0)

    def test_dequeue_back_fail(self):
        dq = DEQueue()
        with self.assertRaises(EmptyDEQueueException):
            dq.dequeue_back()

    def test_front(self):
        dq = DEQueue()
        dq.enqueue_back(0)
        dq.enqueue_back(1)
        self.assertEqual(dq.front(), 0)

    def test_back(self):
        dq = DEQueue()
        dq.enqueue_back(0)
        dq.enqueue_back(1)
        self.assertEqual(dq.back(), 1)

    def test_front_fail(self):
        dq = DEQueue()
        with self.assertRaises(EmptyDEQueueException):
            dq.front()

    def test_back_fail(self):
        dq = DEQueue()
        with self.assertRaises(EmptyDEQueueException):
            dq.back()


if __name__ == '__main__':
    unittest.main()
