from Qimpl import Queue


def checkConsecutivePair(s):
    q = Queue(len(s))
    pairCount = 0
    for i in range(len(s)):
        q.enqueueFromEnd(s[i])
    count = 0
    while(count <= (len(s) - 3)):
        top = q.dequeueFromFront()
        nextFront = q.front()

        checkConsecutive = abs(top - nextFront)
        if(checkConsecutive == 1):
            pairCount += 1
            print "Pair ( %d , %d)" % (top, nextFront)
            print (top)

s = [2, 3, 4, 3, 2, 1, 0, -1, -2, -3]
checkConsecutivePair(s)
