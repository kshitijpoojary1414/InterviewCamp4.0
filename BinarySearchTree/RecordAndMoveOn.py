class RecordAndMoveOn :
    def findFirstOccurenceOfI(self, root):
        current = root
        result = None
        while current is not None :
            if current.val < root.val :
                current = current.left
            elif current.right > root.val :
                current = current.right
            else :
                result = root
                current = current.left

        return result

