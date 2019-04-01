"""
Single linked list node attributes and methods
data
next
get_data
set_data
get_next
set_next
"""

class SLLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


"""
Single linked list attributes and methods
head
next
add_top
add_bot
remove
contains
size
"""

class SLL(object):
    def __init__(self):
        """ initialize an emtpy single linked list """
        self.head = None
        self.next = None

    def add_top(self, data):
        """ add a node containing data to top of list """
        node = SLLNode(data)
        curr = self.head
        self.head = node
        if curr:
            node.set_next(curr)

    def add_bot(self, data):
        """ add a node containing data to bottom of list """
        node = SLLNode(data)
        curr = self.head
        prev = None
        while curr:
            prev = curr
            curr = curr.get_next()
        if prev:
            prev.set_next(node)
        else:
            self.head = node

    def size(self):
        """ return the number of nodes in list """
        cnt = 0
        curr = self.head
        while curr:
            cnt += 1
            curr = curr.get_next()
        return cnt

    def remove(self, node):
        """ delete node from list """
        next = node.get_next()
        if next:
            value = next.get_data()
            node.set_data(value)
            node.set_next(next.get_next())
        else:
            curr = self.head
            prev = None
            while curr.get_next():
                prev = curr
                curr = curr.get_next()
            if prev:
                prev.set_next(None)
            else:
                self.head = None

    def contains(self, data):
        """ returns True if there exists a node containing data """
        found = False
        curr = self.head
        while curr and not found:
            value = curr.get_data()
            if value == data:
                found = True
            else:
                curr = curr.get_next()
        return found
