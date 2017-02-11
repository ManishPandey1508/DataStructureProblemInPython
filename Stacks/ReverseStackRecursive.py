# Reverse the Stack
# Call till the method ends than, save the poped element and thn call a
# method to reverse the top two elements.


def reverseStack(inputStack):
    if(len(inputStack) == 0):
        return
    temp = inputStack.pop()
    reverseStack(inputStack)
    insertAtBottom(inputStack, temp)


def insertAtBottom(inputStack, item):
    if(len(inputStack) == 0):
        inputStack.append(item)
        return
    temp = inputStack.pop()
    insertAtBottom(inputStack, item)
    inputStack.append(temp)

inputStack = []
inputStack.append(35)
inputStack.append(22)
inputStack.append(7)
inputStack.append(15)
inputStack.append(21)
inputStack.append(5)
inputStack.append(99)
inputStack.append(3)
inputStack.append(88)
inputStack.append(7)
print('Origional Stack is ---> ')
print(inputStack)
print('Stack after Reversal')
reverseStack(inputStack)
print(inputStack)