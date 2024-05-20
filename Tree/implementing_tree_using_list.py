class BinaryTree:
    def __init__(self, maxSize):
        self.customList = [None] * maxSize
        self.maxSize = maxSize
        self.lastIndexUsed = 0

    def insertNode(self, value):
        if self.lastIndexUsed + 1 == self.maxSize:
            return "BT is full"
        self.customList[self.lastIndexUsed + 1] = value
        self.lastIndexUsed += 1
        return "node inserted"

    def searchNode(self, nodeValue):
        for i in range(self.lastIndexUsed + 1):
            if self.customList[i] == nodeValue:
                return "Success"
            return "Not Found"

    def preOrderTraversal(self, index):
        if index > self.lastIndexUsed:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastIndexUsed:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index):
        if index > self.lastIndexUsed:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastIndexUsed + 1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastIndexUsed == 0:
            return "Tree is Empty"
        for i in range(1, self.lastIndexUsed + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastIndexUsed]
                self.customList[self.lastIndexUsed] = None
                self.lastIndexUsed -= 1
                return "the node has been deleted"
