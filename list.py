class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.size = 0

    def search(self, key):
        x = self.head
        while x is not None and x.key != key:
            x = x.next
        return x

    def insert(self, key):
        x = Node(key)
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x

    def delete(self, x):
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev

