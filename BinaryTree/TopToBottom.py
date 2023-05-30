class TopToBottom :
    def printAllPaths(self, root):
        if root is None :
            return []

        paths = []
        self.helper(root,paths, [])

    def helper(self, root, paths, currentPath):
        if root is None:
            return

        currentPath.append(root)

        if root.left is None and root.right is None :
            paths.append(currentPath[::])

        self.helper(root.left,paths, currentPath)
        self.helper(root.right,paths, currentPath)
        currentPath.pop()



