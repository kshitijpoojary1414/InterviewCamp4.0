class Successor :
    def findSuccessor(self, node, root):
        if node is None :
            return None

        if node.right is None :
             successor = node.right
             while successor.left is not None :
                successor = successor.left
             return successor
        else :
            rightParent = None 
            successor = root

            while successor is not None :
                if node.val < successor.val :
                    rightParent = successor
                    successor = successor.left
                elif node.val > successor.val :
                    successor = successor.right
                else :
                    break

            return rightParent

        
            