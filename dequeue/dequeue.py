import sys

""" add path for SLL to PYTHONPATH """
sll_path = "/users/alexbroley/github/datastructures/sll"
sys.path.append(sll_path)

from sll.sll import SLL


class EmptyQueueException(Exception):
    """ Exception used when calling a method which needs an element
        but queue is empty """
    pass


"""
Double Ended Queue attributes and methods
items
enqueue_front
enqueue_back
dequeue_front
dequeue_back
front
back
is_empty
length
"""

class DEQueue(object):
    def __init__(self):
        """ initialize empty dequeue """
        self.items = SLL()

    def length(self):
        """ return the number of items in dequeue """
        return self.items.size()

    def is_empty(self):
        """ returns true if there are no items in dequeue """
        return self.length() == 0

    def enqueue_front(self, item):
        """ adds item to the front of dequeue """
        self.items.add_top(item)

    def enqueue_back(self, item):
        """ adds item to the back of dequeue """
        self.items.add_bot(item)

    def dequeue_front(self):
        """ removes and returns item from front of list """
        if self.is_empty():
            raise EmptyQueueException("can not dequeue_front from an empty dequeue")
        else:
            items = self.items
            node = items.head
            value = node.get_data()
            items.remove(node)
            return value

    def dequeue_back(self):
        """ removes and returns item from back of list """
        if self.is_empty():
            raise EmptyQueueException("can not dequeue_back from an empty dequeue")
        else:
            items = self.items
            curr = self.head
            while curr:
                prev = curr
                curr = curr.get_next()
            value = prev.get_data()
            items.remove(prev)
            return value

    def front(self):
        """ returns the value in the front of dequeue """
        if self.is_empty():
            raise EmptyQueueException("can not front from an empty dequeue")
        else:
            items = self.items
            node = items.head
            value = node.get_data()
            return value

    def back(self):
        """ returns the value in the back of dequeue """
        if self.is_empty():
            raise EmptyQueueException("can not back from an empty dequeue")
        else:
            items = self.items
            curr = items.head
            while curr:
                prev = curr
                curr = curr.get_next()
            value = prev.get_data()
            return value
