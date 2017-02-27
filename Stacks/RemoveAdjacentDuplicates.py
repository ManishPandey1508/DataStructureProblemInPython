'''
Given a string, recursively remove adjacent duplicate characters from string. 
The output string should not have any adjacent duplicates. See following examples.

Input:  azxxzy
Output: ay
First "azxxzy" is reduced to "azzy". The string "azzy" contains duplicates, 
so it is further reduced to "ay".
'''
from __builtin__ import str
from xmlrpclib import boolean
from _ast import Str

# Below method I tried to  implement using stack... Its not completely
# working there is still problem in few cases


def removeAdjacentDuplicate(str):
    st = []
    strCounter = 0
    while(strCounter < len(str)):
        if(len(st) == 0):
            st.append(str[strCounter])
            strCounter = strCounter + 1
            print(st)
        else:
            dupCounter = 0
            j = strCounter
            # find the duplicate count
            while(j < len(str) and st[len(st) - 1] == str[j]):
                dupCounter += 1
                j += 1
            if(dupCounter == 0):
                st.append(str[strCounter])
                strCounter += 1
                print(st)
            else:
                for index in range(dupCounter):
                    strCounter += 1

                st.pop()
                print(st)
                dupCounter = 0

    return st

st = ["a", "z", "x", "x", "x", "W", "M", "N", "N", "M", "P", "y"]
print("Input String")
print(st)
print("after removel of adjacent duplicates")
print(removeAdjacentDuplicate(st))
