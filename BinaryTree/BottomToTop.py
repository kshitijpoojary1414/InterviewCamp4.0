class BottomToTop :
    def findHeight(self, root):
        if root is None :
            return -1

        return max(self.findHeight(root.left),self.findHeight(root.right)) + 1

    def isBalanced(self, root):
        if self.helper(root) == -1 :
            return False

        return True

    def helper(self, root):
        if root is None :
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        height = max(left,right) + 1

        if left ==-1 or right == -1 or abs(left-right) > 1:
            return -1

        return height

    def diameter(self, root):
        return self.diameterHelper(root)[1]

    def diameterHelper(self, root):
        if root is None:
            return (-1, 0)

        left = self.diameter(root.left)
        right = self.diameter(root.right)

        maxDiameter = max(left[1], right[1], left[0] + right[0] + 1)

        height = 1 + max(left[0], right[0])

        return (height, maxDiameter)


