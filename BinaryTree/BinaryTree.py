class BinaryTree :
    def inorder(self, root):
        if root is None :
            return root

        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return root

        print(root.val)
        self.inorder(root.left)
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return root

        self.inorder(root.left)
        self.inorder(root.right)
        print(root.val)

    def inorderIterative(self, root):
        if root is None :
            return root

        stack = [root]
        result = []
        visited = set()
        while len(stack) > 0 :
            node = stack.pop()

            if node in visited :
                result.append(node.val)
            else :
                visited.add(node)

                if node.right is not None :
                    stack.append(node.right)

                stack.append(node)

                if node.left is not None :
                    stack.append(node.left)
