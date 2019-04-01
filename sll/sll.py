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

    
