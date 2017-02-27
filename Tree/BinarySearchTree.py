
class Node:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = None

    def insert(self, data):
        if(data == self.data):
            return False
        elif(data < self.data):
            if(self.leftChild):
                return self.leftChild.insert(data)
            else:
                temp = Node(data)
                temp.parent = self
                self.leftChild = temp
                return True
        else:
            if(self.rightChild):
                return self.rightChild.insert(data)
            else:
                temp = Node(data)
                temp.parent = self
                self.rightChild = temp
                return True

    def find(self, data):
        if(self.data == data):
            return self
        elif(data < self.data):
            if(self.leftChild):
                return self.leftChild.find(data)
            else:
                return false
        elif(data > self.data):
            if(self.rightChild):
                return self.rightChild.find(data)
        else:
            return False
# Root--> Left --> right

    def preOrder(self):
        if(self):
            print (str(self.data))
            if(self.leftChild):
                self.leftChild.preOrder()
            if(self.rightChild):
                self.rightChild.preOrder()
# left-->Root-->Right

    def inOrder(self):
        if(self):
            if(self.leftChild):
                self.leftChild.inOrder()
            print (str(self.data))
            if(self.rightChild):
                self.rightChild.inOrder()

# Left-->right-->root

    def postOrder(self):
        if(self):
            if(self.leftChild):
                self.leftChild.postOrder()
            if(self.rightChild):
                self.rightChild.postOrder()
            print (str(self.data))


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if(self.root):
            return self.root.find(data)
        else:
            return False

    def preOrder(self):
        print("Pre-Order Traversal")
        if(self.root):
            return self.root.preOrder()
        else:
            return False

    def postOrder(self):
        print("Post-Order Traversal")
        if(self.root):
            return self.root.postOrder()
        else:
            return False

    def inOrder(self):
        print("In-Order Traversal")
        if(self.root):
            return self.root.inOrder()
        else:
            return Fals

  # Method to find least Common Ancestor Node
    def findLCA(self, rootNode, nodeA, nodeB):
        if(rootNode.data < nodeA.data and rootNode.data < nodeB.data):
            return self.findLCA(rootNode.rightChild, nodeA, nodeB)
        elif(rootNode.data > nodeA.data and rootNode.data > nodeB.data):
            return self.findLCA(rootNode.leftChild, nodeA, nodeB)
        else:
            return rootNode

    def pathToLCA(self, startNode, lcaNode):
        pathList = []
        while startNode.data != lcaNode.data:
            pathList.append(startNode.data)
            startNode = startNode.parent
        return pathList

    def pathBetweenTwoNode(self, startNode, endNode):
        lcaNode = self.findLCA(bst.root, startNode, endNode)
        startToLca = self.pathToLCA(startNode, lcaNode)
        endToLca = self.pathToLCA(endNode, lcaNode)
        print startToLca
        print lcaNode.data
        print endToLca


bst = Tree()
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(3)
bst.insert(1)
bst.insert(4)
bst.insert(11)
bst.insert(9)
bst.insert(12)

bst.preOrder()

bst.inOrder()

bst.postOrder()

temp = bst.findLCA(bst.root, Node(1), Node(12))
print "LCA is :"
startNode = bst.find(1)
endNode = bst.find(7)
print bst.pathBetweenTwoNode(startNode, endNode)
