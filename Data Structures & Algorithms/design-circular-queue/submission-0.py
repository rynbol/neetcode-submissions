class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularQueue:

    def __init__(self, k: int):
        # Two sentinel nodes, wired to each other so the list is never "empty"
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
            
        node = Node(value)
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        first = self.head.next
        self.head.next = first.next
        first.next.prev = self.head

        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k