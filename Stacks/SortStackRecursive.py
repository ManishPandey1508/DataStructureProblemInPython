'''

'''


def sortingStack(st):
    if(len(st) == 0):
        return
    temp = st.pop()
    sortingStack(st)
    insertInSortedStack(st, temp)
    return st


def insertInSortedStack(st, temp):
    if(len(st) == 0 or st[len(st) - 1] < temp):
        st.append(temp)
    else:
        x = st.pop()
        insertInSortedStack(st, temp)
        st.append(x)

stack = [2, 4, 9, 6, 1, 22, 45, 32, 23, 70]
print "Unsorted Array"
print stack
st = sortingStack(stack)
print "Sorted Array"
print st
