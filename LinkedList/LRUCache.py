from LinkedList.LinkedHashTable import LinkedHashTable

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linkedHT = LinkedHashTable()

    def get(self, key):
        node = self.linkedHT.get(key)
        if node is None:
            return -1

        self.linkedHT.remove(key)
        self.linkedHT.add(key, node.val)
        return node.val

    def put(self, key, val):
        if self.linkedHT.get(key) is None and self.linkedHT.size == self.capacity:
            tail = self.linkedHT.tail.prev
            self.linkedHT.remove(tail.key)
        self.linkedHT.add(key, val)

