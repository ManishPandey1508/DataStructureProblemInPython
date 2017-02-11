'''
Create an empty stack called opstack for keeping operators. Create an empty list for output.
Convert the input infix string to a list by using the string method split.
Scan the token list from left to right.
If the token is an operand, append it to the end of the output list.
If the token is a left parenthesis, push it on the opstack.
If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.
If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence
 and append them to the output list.
When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.
'''
def peek(anyStack):
         return anyStack[len(anyStack) - 1]

def infixToPostfix(infixexpr):
   # dictionary to check precedence
    opPrecedence = {}
    opPrecedence["*"] = 3
    opPrecedence["/"] = 3
    opPrecedence["+"] = 2
    opPrecedence["-"] = 2
    opPrecedence["("] = 1
    
    operatorSet = set(['*', '/', '(', ')', '+', '-'])
    # List to save 
    opStack = []
    postFixList = []
    tokenList = infixexpr.split()
    for token in tokenList:
        # check if token is in alphabet or Number put that in postfixList
        if  token not in operatorSet :
            postFixList.append(token)
            # else check if token == '(' put that token in opstack
        elif token == '(':  
            opStack.append(token)
            # else check if token ==')' take all element out from opstack till '(' found
        elif token == ')':
            topToken = opStack.pop()
            while(topToken != '('):
                postFixList.append(topToken)
                topToken = opStack.pop()
         # else if while opstack is not empty and token precedence is 
         # less than top most element precedence in opstack take out ll the elements till this condition satisfy          
        else:
            while(not len(opStack) == 0) and (opPrecedence[peek(opStack)] >= opPrecedence[token]):
                postFixList.append(opStack.pop())
            opStack.append(token)
    while (len(opStack) != 0):
        postFixList.append(opStack.pop())
    return " ".join(postFixList)            
# print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    
