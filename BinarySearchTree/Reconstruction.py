class Reconstruction :
    def createBST(self, arr):
        return self.helper(arr, 0, len(arr)-1)

    def helper(self, arr, start, end):
        if end < start :
            return None

        mid = start + (end-start)//2

        root = Node(mid)

        root.left = self.helper(arr,0,mid - 1)
        root.right = self.helper(arr,mid + 1,len(arr)-1)

        return root