class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LinkedHashTable:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.map = {}
        self.size = 0

    def get(self, key):
        if key in self.map:
            return self.map[key]

    def add(self, key, value):
        node = Node(key, value)
        if key in self.map:
            self.remove(key)

        self.map[key] = node
        self.appendToLinkedList(node)
        self.size += 1

    def remove(self, key):
        toDelete = self.map[key]
        del self.map[key]
        self.deleteFromLinkedList(toDelete)
        self.size -= 1

    def size(self):
        return self.size

    def appendToLinkedList(self, node):
        next = self.head.next
        node.next = next
        self.head.next = node
        next.prev = node
        node.prev = self.head

    def deleteFromLinkedList(self, toDelete):
        prev = toDelete.prev
        next = toDelete.next
        prev.next = toDelete.next
        next.prev = toDelete.prev

    def head(self):
        return self.head

    def tail(self):
        return self.tail

