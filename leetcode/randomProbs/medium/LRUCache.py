class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = Node(0, 0)
        self.next = Node(0, 0)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.tail.prev = self.head
        self.head.next = self.tail


    def get(self, key: int) -> int:
        if key in self.dict:
            n = self.dict[key]
            self.remove(n)
            self.add(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        if (key in self.dict):
            self.remove(self.dict[key])
        n = Node(key, value)
        self.dict[key] = n
        self.add(n)
        if (self.capacity < len(self.dict)):
            n = self.head.next
            self.remove(n)
            del self.dict[n.key]


    def add(self, n):
        p = self.tail.prev
        p.next = n
        self.tail.prev = n
        n.prev = p
        n.next = self.tail

    def remove(self, n):
        n.prev.next = n.next
        n.next.prev = n.prev
