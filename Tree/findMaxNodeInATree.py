from BinaryTree import BinaryTree
from BinaryTree import Node

# Recursive


def findMaxNodeInABinaryTreeRecursive(rootNode):
    maxNode = None
    if(rootNode != None):
        maxLeft = findMaxNodeInABinaryTreeRecursive(rootNode.leftChild)
        maxRight = findMaxNodeInABinaryTreeRecursive(rootNode.rightChild)

        if(maxLeft > maxRight):
            maxNode = maxLeft
        else:
            maxNode = maxRight

        if(rootNode > maxNode):
            maxNode = rootNode
    return maxNode


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
node11 = tree.setRightChild(node9, Node(55))
node10 = tree.setLeftChild(node9, Node(45))

tree.postOrderTraversal()
print "Max Node in the tree"
t = findMaxNodeInABinaryTreeRecursive(tree.getRootNode())
print t.data
