
class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        pass

    def insertNode(self, root,data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                root.left = self.insertNode(root.left, data)
            else:
                root.right = self.insertNode(root.right, data)
        return root

    def searchNode(self, value_to_search):
        pass

    def updateNode(self, value_to_update):
        pass

    def viewNodes(self, root):
        
        if root:
            print(root.data, end=" ")
            self.viewNodes(root.left)
            self.viewNodes(root.right)


if __name__=='__main__':
    # execute code here
    bst = BinaryTree()
    rootPtr = None
    for _ in range(5):
        data = int(input())
        rootPtr = bst.insertNode(rootPtr, data)
    
    print(rootPtr)
    print(rootPtr.data)
    bst.viewNodes(rootPtr)
