'''
Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull() 
and an additional operation getMin() which should return minimum element from the SpecialStack. All these operations 
of SpecialStack must be O(1). To implement SpecialStack, you should only use standard Stack data structure and no other
 data structure like arrays, list, .. etc
 '''
# create two stacks, one regular stack and one stack to store minimimum value such that on top always the minimumm
# value get stored


class Stack():

    def itemPeek(self):
        return self.items[len(self.items) - 1]

    def auxPeek(self):
        return self.auxStack[len(self.auxStack) - 1]

    def __init__(self):
        self.items = []
        self.auxStack = []

    def isEmptySelf(self):
        return self.items == []

    def isEmptyAux(self):
        return self.auxStack == []
# check if both stacks empty, if yes push same item in both stacks.

    def push(self, item):
        self.items.append(item)
        if(self.isEmptyAux()):
            self.auxStack.append(item)
        elif(self.auxPeek() < item):
            self.auxStack.append(self.auxPeek())
        else:
            self.auxStack.append(item)
        print self.auxStack

    def popItem(self):
        self.auxStack.pop()
        return self.items.pop()

    def getElements(self):
        return self.items

    def getAuxElements(self):
        return self.items

    def getMinElement(self):
        return self.auxPeek()

stack = Stack()
stack.push(35)
stack.push(22)
stack.push(7)
stack.push(15)
stack.push(21)
stack.push(5)
stack.push(99)
stack.push(3)
stack.push(88)
stack.push(7)

print "Main Stack elements -->> "
print stack.getElements()
print stack.getAuxElements()
print stack.getMinElement()
