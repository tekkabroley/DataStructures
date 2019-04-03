import sys

""" add path for SLL to PYTHONPATH """
sll_path = "/users/alexbroley/github/datastructures/sll"
sys.path.append(sll_path)

from sll.sll import SLL


"""
Stack attributes and methods
items
is_empty
push
pop
top
depth
"""

class Stack(object):
    """ stack implementation utilizing my single linked list """
    def __init__(self):
        """ initializes stack with empty single linked list """
        self.items = SLL()

    def is_empty(self):
        """ returns True if stack is empty """
        return items.size() == 0

    def push(self, item):
        """ adds item to stack """
        self.items.add_top(item)

    def pop(self):
        if not self.is_empty():
            node = self.items.head
            item = node.get_data()
            self.items.remove(node)
            return item
        else:
            raise Exception("trying to pop from an empty stack")

    def top(self):
        if not self.is_empty():
            node = self.items.head
            item = node.get_data()
            return item
        else:
            raise Exception("trying to top from an empty stack")

    def depth(self):
        return self.items.size()
