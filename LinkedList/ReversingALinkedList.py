class ReversingALinkedList :
    def reverse(self, head):
        prev = None
        current = head
        while current is not None :
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode

        return prev

    def isPalindrome(self, head) -> bool:
        originalHead = head
        fast = head
        slow = head

        if head is None :
            return None

        while fast.next is not None :
            fast = fast.next
            if fast.next is not None :
                fast = fast.next
                slow = slow.next

        slow = slow.next
        slow = self.reverseList(slow)

        while slow is not None :
            if slow.val != originalHead.val :
                return False
            slow = slow.next
            originalHead = originalHead.next


        return True

