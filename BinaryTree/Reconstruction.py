class Reconstruction :
    def reconstruction(self, inorder, preorder):
        inorderMap = {}

        for i in range(len(inorder)) :
            val = inorder[i]
            inorderMap[val] = i

        return self.construct(0, len(inorder)-1, inorder, 0, len(preorder)-1, preorder, inorderMap)

    def construct(self, inStart, inEnd, inorder, preStart, preEnd, preorder, inorderMap):
        if inEnd < inStart or preEnd < preStart :
            return None

        root = preorder[0]
        rootIndex = inorderMap[root]
        root = Node(root)

        root.left = self.construct(inStart, rootIndex - 1 , inorder , preStart + 1, preStart +(rootIndex - inStart), preorder, inorderMap)
        root.right = self.construct(inStart, rootIndex + 1 , inorder , preStart + 1 +(rootIndex - inStart), preEnd, preorder, inorderMap)

        return root