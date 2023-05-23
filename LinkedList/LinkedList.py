class Node :
    def __init(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList :
    def __init__(self, head, tail):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail

    def append(self, toAdd):
        toAdd.next = self.head.next
        self.head.next = toAdd

    def deleteWithoutPrev(self, node):
        next = node.next
        if next is None :
            return

        self.node.val = self.next.val
        self.delete(next, node)

    def delete(self, toDelete, prev):
        prev.next = toDelete.next

    def oddEven(self, head):
        if head is None :
            return None

        current = head
        currentIndex = 0
        odd = LinkedList()
        even = LinkedList()

        while current != None :
            currentIndex += 1

            if currentIndex %2 == 0 :
                even.append(current)
            else :
                odd.append(current)

            current = current.next

        return (odd,even)