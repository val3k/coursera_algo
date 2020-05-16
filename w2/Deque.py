class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class Deque():
    def __init__(self):
        self.size = 0
        self.first = Node(None)
        self.last = self.first
        self.current = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            self.current = self.first
        item = self.current.item
        self.current = self.current.next
        if self.current is None:
            raise StopIteration
        return item

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, item):
        oldfirst = self.first
        self.first = Node(item)
        self.first.next = oldfirst
        self.size += 1

    def addLast(self, item):
        oldlast = self.last
        self.last = Node(item)
        self.last.next = None
        oldlast.next = self.last
        self.last.prev = oldlast
        self.size += 1

    def removeFirst(self):
        item = self.first.item
        self.first = self.first.next
        self.size -= 1
        print(item)

    def removeLast(self):
        item = self.last.item
        self.last = self.last.prev
        self.size -= 1
        print(item)


class linkedList():
    def __init__(self):
        self.first = Node(None)
        self.oldfirst = None
        self.size = 0

    def isEmpty(self):
        return self.first is None

    def push(self, item):
        self.oldfirst = self.first
        self.first = Node(item)
        self.first.next = self.oldfirst
        self.size += 1

    def pop(self):
        item = self.first.item
        self.first = self.first.next
        self.size -= 1
        print(item)


ll = Deque()
in_s = 'abcdZYXW'
for i in in_s:
    if i == '-':
        ll.removeFirst()
    elif i == '_':
        ll.removeLast()
    elif i.isupper():
        ll.addLast(i)
    else:
        ll.addFirst(i)

for i in ll:
    print(i)






