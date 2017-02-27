from QueueProbs.Qimpl import Queue


class Node:
    # initilize Binary tree

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def deleteTree(self):
        self.root = None

    def getRootNode(self):
        if(self.root != None):
            return self.root
        else:
            return None

    def setRootNode(self, node):
        self.root = node
        return self.root

    def setLeftChild(self, thisNode, newNode):
        if(thisNode.leftChild == None):
            thisNode.leftChild = newNode
            newNode.parent = thisNode
        return newNode

    def setRightChild(self, thisNode, newNode):
        if(thisNode.rightChild == None):
            thisNode.rightChild = newNode
            newNode.parent = thisNode
        return newNode

    def deleteLeftChild(self, thisNode):
        if(thisNode.leftChild != None):
            thisNode.leftChild = None

    def deleteRightChild(self, thisNode):
        if(thisNode.rightChild != None):
            thisNode.rightChild = None

    def getLeftChild(self, thisNode):
        if(thisNode.leftChild != None):
            return thisNode.leftChild

    def getRightChild(self, thisNode):
        if(thisNode.rightChild != None):
            return thisNode.rightChild

    def preOrderTraversal(self):
        if(self.isEmpty()):
            print "Tree is Empty traversal Not possible"
        else:
            # Stack Used
            tempStack = []
       # outPut List
            preOrderList = []
# Prcess root
            if(self.root):
                preOrderList.append(self.root.data)
                if(self.root.rightChild):
                    tempStack.append(self.root.rightChild)
                if(self.root.leftChild):
                    tempStack.append(self.root.leftChild)
            while(len(tempStack) != 0):
                temp = tempStack.pop()
                preOrderList.append(temp.data)
                if(temp.rightChild):
                    tempStack.append(temp.rightChild)
                if(temp.leftChild):
                    tempStack.append(temp.leftChild)
        print preOrderList

    def postOrderTraversal(self):
        if(self.isEmpty()):
            print "Tree is Empty traversal Not possible"
        else:
            # two  Stack Used
            tempStack1st = []
            tempStack2nd = []
            postOrderist = []
            # Process root
        if(self.root):
            tempStack1st.append(self.root)
            while(len(tempStack1st) != 0):
               # pop out the top node
                temp = tempStack1st.pop()
                # put top node in final stack
                tempStack2nd.append(temp.data)
                # put left child of the popped out node in the stack
                if(temp.leftChild):
                    tempStack1st.append(temp.leftChild)
                # put right child of the popped out node in the stack
                if(temp.rightChild):
                    tempStack1st.append(temp.rightChild)
        for i in range(len(tempStack2nd)):
            postOrderist.append(tempStack2nd.pop())
        print postOrderist

    def inOrderTraversal(self):
        if(self.isEmpty()):
            print "Tree is Empty traversal Not possible"
        else:
            # One temporary Stack Used
            tempStack = []
            # Temporary variable to store root of subtrees
            rootNode = None
            # print List
            listToPrint = []
            # Process root
            if(self.root):
                rootNode = self.root
                treeComplete = False
                while(not treeComplete):
                    if(rootNode != None):
                        tempStack.append(rootNode)
                        rootNode = rootNode.leftChild
                    elif(rootNode == None and len(tempStack) != 0):
                        temp = tempStack.pop()
                        listToPrint.append(temp.data)
                        rootNode = temp.rightChild
                    elif(len(tempStack) == 0):
                        treeComplete = True
            print listToPrint

    def levelOrderTraversal(self):
        listToPrint = []
        q = Queue(10)
        if(self.isEmpty()):
            print "Tree is Empty traversal Not possible"
        else:
            if(self.root):
                q.enqueueFromEnd()
            while(not q.isEmpty()):
                temp = q.dequeueFromFront()
                listToPrint.append(temp.data)
                if(temp.leftChild != None):
                    q.enqueueFromEnd(temp)
                if(temp.righChild != None):
                    q.enqueueFromEnd(temp)
        print listToPrint

tree = BinaryTree()
rootNode = tree.setRootNode(Node(10))
left2root = tree.setLeftChild(rootNode, Node(11))
right2root = tree.setRightChild(rootNode, Node(-20))
leftAtLevel2 = tree.setLeftChild(left2root, Node(15))
rightAtLevel2 = tree.setRightChild(left2root, Node(12))
node6 = tree.setRightChild(right2root, Node(9))
node7 = tree.setLeftChild(right2root, Node(0))
node8 = tree.setRightChild(node7, Node(18))
node9 = tree.setLeftChild(node7, Node(16))

tree.levelOrderTraversal()
