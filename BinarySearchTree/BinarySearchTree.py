class Node :
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree :
    def isBst(self, root):
        return self.helper(root, float("-inf"), float('inf'))
    def helper(self, root, min, max):
        if root is None :
            return True

        if root.val < min and root.val > max :
            return False

        return self.helper(root.left, min, root.val) and self.helper(root.right, root.val , max)

    def __init__(self):
        self.root = None

    def add(self, value):
        parent = None
        current = self.root

        while current is not None :
            parent = current
            if value > current.val :
                current = current.right
            else :
                current = current.left

        if parent is None :
            self.root = Node(value)
        elif value < parent.val :
            parent.left = Node(value)
        else :
            parent.right = Node(value)

    def search(self, value):
        current = self.root

        while current is not None :
            if current.val == value :
                return True
            if value > current.val :
                current = current.right
            else :
                current = current.left

        return False
    def replaceChild(self, parent, oldChild, newChild):
        if parent is None :
            self.root = newChild
        elif parent.left == oldChild :
            parent.left = newChild
        elif parent.right == oldChild :
            parent.right = oldChild

    def deleteNode(self, node, parent):
        if node.left is None and node.right is None :
            self.replaceChild(parent, node, None )
        elif node.left is None and node.right is not None :
            self.replaceChild(parent, node, node.right)
        elif node.right is  None and node.left is not None :
            self.replaceChild(parent, node, node.left)
        else :
            successor = self.root
            successorParent = None

            while successor.left is not None :
                successorParent = successor
                successor = successor.left
            node.val = successor.val
            self.deleteNode(successorParent, successor)









