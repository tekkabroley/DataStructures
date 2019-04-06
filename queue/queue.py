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
Queue attributes and methods
items
enqueue
dequeue
front
is_empty
length
"""

class Queue(object):
    def __init__(self):
        """ initialize single linked list """
        self.items = SLL()

    def length(self):
        """ returns the number of items in queue"""
        return self.items.size()

    def is_empty(self):
        """ returns True if queue is empty """
        return self.length() == 0

    def enqueue(self, item):
        """ adds an element to the back of queue """
        self.items.add_bot(item)

    def dequeue(self):
        """ removes item from head of queue and returns item """
        if self.is_empty():
            raise EmptyQueueException("trying to dequeue from an empty queue")
        else:
            items = self.items
            node = items.head
            item = node.get_data()
            items.remove(node)
            return item

    def front(self):
        """ returns the item in the head of queue """
        if self.is_empty():
            raise EmptyQueueException("trying to front from an empty queue")
        else:
            item = self.items.head.get_data()
            return item
