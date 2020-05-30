from Deque import Node
from random import randint


class RandomizedQueue():
    def __init__(self):
        self.size = 0
        self.first = Node(None)
        self.last = None
        self.current = None

    def __iter__(self):
        return self

    def __next__(self):
        # start iteration from first
        if self.current is None:
            self.current = self.first
        item = self.current.item
        if item is None:
            raise StopIteration
        self.current = self.current.next
        # create empty node for stop iteration
        if self.current is None:
            self.current = Node(None)
        return item

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return self.size

    def enqueue(self, item):
        if item is None:
            raise ValueError('item is None, pass not null value')
        if self.first.item is None:
            self.first.item = item
            self.size += 1
        else:
            oldfirst = self.first
            self.first = Node(item)
            self.first.next = oldfirst
            self.size += 1

    def dequeue(self):
        cur = self.first
        num = randint(0, self.size-1)
        if num == 0:
            item = self.first.item
            self.first = self.first.next
            self.size -= 1
            return item
        for i in range(num+1):
            if i + 1 == num:
                to_del = cur.next
                item = to_del.item
                cur.next = to_del.next
                self.size -= 1
                return item
            else:
                cur = cur.next

    def sample(self):
        num = randint(0, self.size-1)
        cur = self.first
        for i in range(num+1):
            if i == num:
                return cur.item
            else:
                cur = cur.next
