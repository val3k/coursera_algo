class Node():
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

    def addLast(self, item):
        if item is None:
            raise ValueError('item is None, pass not null value')
        if self.last.item is None:
            self.last.item = item
            self.size += 1
        else:
            oldlast = self.last
            self.last = Node(item)
            self.last.next = None
            oldlast.next = self.last
            self.last.prev = oldlast
            self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            raise ValueError('no items to remove')
        else:
            item = self.first.item
            self.first = self.first.next
            self.size -= 1
            print(item)

    def removeLast(self):
        if self.isEmpty():
            raise ValueError('no items to remove')
        else:
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
in_s = 'abcdLADR-----'
for i in in_s:
    if i == '-':
        ll.removeFirst()
    elif i == '_':
        ll.removeLast()
    elif i.isupper():
        ll.addLast(i)
    else:
        ll.addFirst(i)
