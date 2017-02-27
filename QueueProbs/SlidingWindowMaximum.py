
'''
A long array A[] is given to you. There is a sliding window of size w which is moving from the very left of the array to the very right. You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position. Following is an example:
The array is [1 3 -1 -3 5 3 6 7], and w is 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Input: A long array A[], and a window width w
Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
Requirement: Find a good optimal way to get B[i]

http://www.ideserve.co.in/learn/maximum-element-from-each-subarray-of-size-k-set-2
'''
from Qimpl import Queue

a = [9, 6, 11, 8, 10, 5, 14, 13, 93, 14]
11,


def slidingWindowMax(a, k):
    q = Queue(k)
    for i in range(k):
        while (not q.isEmpty() and a[q.rear()] < a[i]):
            q.dequeueFromEnd()
        q.enqueuefromFront(i)

    for j in range(4, len(a)):
        print(a[q.rear()])
        while(not q.isEmpty() and q.rear() < j - k + 1):
            q.dequeueFromEnd()
        while (not q.isEmpty() and a[q.front()] < a[j]):
            q.dequeueFromFront()
        q.enqueuefromFront(j)

slidingWindowMax(a, 4)
