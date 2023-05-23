class SlowAndFastPointer :
    def hasCycle(self, head):
        if head is None :
            return None

        fast = head
        slow = head

        while fast.next is not None :
            fast = fast.next

            if fast == slow :
                return True

            if fast is not None :
                fast = fast.next
                if fast == slow :
                    return True

            slow = slow.next

        return False

    def lengthOfCycle(self, head):
        if head is None :
            return None

        fast = head
        slow = head

        while fast.next is not None :
            fast = fast.next

            if fast == slow :
                break
            if fast is not None :
                fast = fast.next
                if fast == slow :
                    break

            slow = slow.next

        fast = fast.next
        nodesPassed = 1

        while fast != slow :
            fast = fast.next
            nodesPassed += 1

        return nodesPassed

    def findMedian(self, head):
        if head is None :
            return None

        fast = head
        slow = head

        while fast.next != None :
            fast = fast.next
            if fast is not None :
                fast = fast.next
                slow = slow.next

        return slow

    def findBeginingOfCycle(self, head):
        length = self.lengthOfCycle(head)

        fast = head
        slow = head
        while length > 0 :
            fast = fast.next
            length -= 1

        while fast != slow :
            fast = fast.next
            slow = slow.next

        return slow