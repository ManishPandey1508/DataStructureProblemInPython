
class Queue:

    def __init__(self, maxItems=0):
        self.items = []
        self.maxSize = maxItems

    def enqueueFromEnd(self, item):
        if(self.isFull()):
            print "Queue is Full, item can not be intersted"
        else:
            self.items.insert(0, item)

    def enqueuefromFront(self, item):
        if(self.isFull()):
            print "Queue is Full, item can not be intersted"
        else:
            self.items.append(item)

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.maxSize

    def dequeueFromFront(self):
        if(self.isEmpty()):
            print "Queue is empty, item can be removed "
        else:
            return self.items.pop()

    def dequeueFromEnd(self):
        if(self.isEmpty()):
            print ""
        else:
            self.items.pop(0)

    def queueSize(self):
        return len(self.items)

    def printQueue(self):
        for i in range(len(self.items)):
            print "{} -->".format(self.items[i])

    def front(self):
        return self.items[-1]

    def rear(self):
        return(self.items[0])
