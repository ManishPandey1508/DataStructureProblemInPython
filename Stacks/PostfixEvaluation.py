
# define a stack

# for all token in ppost fix epxression

# if token is operand put it in stack

# if token is operator fetch last two operands and perform operation and put result in stack

# repeat these two steps till token exists.

def postFixEval(postFixExpr):
    
    tokenList = postFixExpr.split()
    opStack = []
    operatorSet = set(['*', '/', '(', ')', '+', '-'])
    
    for token in tokenList:
        if token not in operatorSet:
            opStack.append(token)
        else:
            temp1 = int(opStack.pop())
            temp2 = int(opStack.pop())
            if(token == '*'):
                opStack.append(temp1 * temp2)
            elif(token == '/'):
                opStack.append(temp2 / temp1)
            elif(token == '+'):
                opStack.append(temp1 + temp2)
            elif(token == '-'):
                opStack.append(temp2 - temp1)
    temp3 = opStack.pop()
    return temp3
    
print(postFixEval('6 8 2 / 1 - *'))

