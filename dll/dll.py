"""
Double linked list node attributes and methods
data
next
prev
get_data
set_data
get_next
set_next
get_prev
set_prev
"""

class DLLNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def get_prev(self):
        return self.prev

    def set_prev(self, node):
        self.prev = node


"""
Double linked list attributes and methods
head
add_top
add_bot
remove
contains
size
"""

class DLL(object):
    def __init__(self):
        """ initialize empty double linked list """
        self.head = None

    def add_top(self, data):
        """ add node containing data to top of list """
        node = DLLNode(data)
        curr = self.head
        self.head = node
        if curr:
            node.set_next(curr)
            curr.set_prev(node)

    def add_bot(self, data):
        """ add node containing data to bottom of list """
        node = DLLNode(data)
        curr = self.head
        prev = None
        while curr:
            prev = curr
            curr = curr.get_next()
        if prev:
            prev.set_next(node)
            node.set_prev(prev)
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
        prev = node.get_prev()
        next = node.get_next()
        if prev and next:
            prev.set_next(next)
            next.set_prev(prev)
        elif prev:
            prev.set_next(None)
        elif next:
            self.head = next
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
