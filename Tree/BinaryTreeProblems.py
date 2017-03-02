from QueueProbs.Qimpl import Queue

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxDepth(node):
    if node is None:
        return 0;
    else:
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1

def maxDepthIterative(node):
    q = Queue(10)
    depth = 0
    if root is None:
        print "Tree depth is zero there is no root"
    else:
        q.enqueueFromEnd(node)
        while(True):
            nodeCount = q.queueSize()
            if nodeCount is 0:
                return depth
            depth+=1
            while(nodeCount > 0):
                temp = q.dequeueFromFront()
                if(temp.left != None):
                    q.enqueueFromEnd(temp.left)
                if(temp.right!=None):
                    q.enqueueFromEnd(temp.right)
                nodeCount -= 1

def minDepthIterative(node):
    q = Queue(10)
    depth = 0
    if root is None:
        print "Tree depth is zero there is no root"
    else:
        q.enqueueFromEnd(node)
        while(True):
            nodeCount = q.queueSize()
            if nodeCount is 0:
                return depth
            depth+=1
            while(nodeCount > 0):
                temp = q.dequeueFromFront()
                if(temp.left== None and temp.right==None):
                    return depth
                if(temp.left != None):
                    q.enqueueFromEnd(temp.left)
                if(temp.right!=None):
                    q.enqueueFromEnd(temp.right)
                nodeCount -= 1


global maxNode

def findMaxNodeInABinaryTreeRecursive(rootNode):
    if rootNode != None:
        maxLeft = findMaxNodeInABinaryTreeRecursive(rootNode.left)
        maxRight = findMaxNodeInABinaryTreeRecursive(rootNode.right)
        if (maxLeft > maxRight):
            maxNode = maxLeft
        else:
            maxNode = maxRight
        if (rootNode.data > maxNode):
            maxNode = rootNode.data
        return maxNode

        # Searching an Element a tree recursive

def searchElemenRecursive(root, data):
    if root == None:
        return False
    if root.data == data:
        return True
    leftBool = searchElemenRecursive(root.left, data)
    rightBool = searchElemenRecursive(root.right, data)
    return leftBool or rightBool

    # Searching an Element a tree recursive


def sizeOfTreeRecusrive(root):
    count = 0
    if root == None:
        return count
    else:
        return 1 + sizeOfTreeRecusrive(root.left) + sizeOfTreeRecusrive(root.right)


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(11)
root.right.right = Node(12)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)

print "Height of tree is %d" % (maxDepth(root))
print "Height of tree iterative is %d" % (maxDepthIterative(root))
print "Max Node of the tree is %d" % (findMaxNodeInABinaryTreeRecursive(root))
print "Size of Tree found recursively is %d" %(sizeOfTreeRecusrive(root))
print "Element 4 exist in Tree %d" %(searchElemenRecursive(root,4))
print "Minimum depth if the Tree is %d" %(minDepthIterative(root))