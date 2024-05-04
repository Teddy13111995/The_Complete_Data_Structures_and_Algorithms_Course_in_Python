class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
leftChildHot = TreeNode("Tea")
rightChildHot = TreeNode("Coffee")
leftChildCold = TreeNode("Non-alcoholic")
rightChildCold = TreeNode("Alcoholic")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
leftChild.leftChild = leftChildHot
leftChild.rightChild = rightChildHot
rightChild.rightChild = rightChildCold
rightChild.leftChild = leftChildCold


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


preOrderTraversal(newBT)

print("\n")


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


inOrderTraversal(newBT)

print("\n")


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


postOrderTraversal(newBT)
