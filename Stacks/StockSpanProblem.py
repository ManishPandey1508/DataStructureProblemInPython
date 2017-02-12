
def calculateSpan(price, n, span):
    span[0] = 1
    st = []
    st.append(0)
    for i in range(1, n, 1):
        while(len(st) >= 1 and price[st[len(st) - 1]] <= price[i]):
            st.pop()
        if(len(st) == 0):
            span[i] = i + 1
        else:
            span[i] = i - st[len(st) - 1]
        st.append(i)

# A utility function to print elements of array


def printArray(arr, n):

    for i in range(n):
        print(arr[i])

# Driver program to test above function
price = [10, 4, 5, 90, 120, 80]
n = len(price)
S = [None] * n

# Fill the span values in list S[]
calculateSpan(price, n, S)

# print the calculated span values
printArray(S, n)
