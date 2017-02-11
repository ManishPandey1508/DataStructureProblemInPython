'''
1. While there are still tokens to be read in,
   1.1 Get the next token.
   1.2 If the token is:
       1.2.1 A number: push it onto the value stack.
       1.2.2 A variable: get its value, and push onto the value stack.
       1.2.3 A left parenthesis: push it onto the operator stack.
       1.2.4 A right parenthesis:
         1 While the thing on top of the operator stack is not a 
           left parenthesis,
             1 Pop the operator from the operator stack.
             2 Pop the value stack twice, getting two operands.
             3 Apply the operator to the operands, in the correct order.
             4 Push the result onto the value stack.
         2 Pop the left parenthesis from the operator stack, and discard it.
       1.2.5 An operator (call it thisOp):
         1 While the operator stack is not empty, and the top thing on the
           operator stack has the same or greater precedence as thisOp,
           1 Pop the operator from the operator stack.
           2 Pop the value stack twice, getting two operands.
           3 Apply the operator to the operands, in the correct order.
           4 Push the result onto the value stack.
         2 Push thisOp onto the operator stack.
2. While the operator stack is not empty,
    1 Pop the operator from the operator stack.
    2 Pop the value stack twice, getting two operands.
    3 Apply the operator to the operands, in the correct order.
    4 Push the result onto the value stack.
3. At this point the operator stack should be empty, and the value
   stack should have only one value in it, which is the final result.
   '''
def peek(infixStr):
    return infixStr[len(infixStr) - 1]   
   
def infixEvalOneCycle(inExpr):
    opStack = []
    valueStack = []
    print inExpr
    opPrecedence = {}
    opPrecedence["*"] = 3
    opPrecedence["/"] = 3
    opPrecedence["+"] = 2
    opPrecedence["-"] = 2
    opPrecedence["("] = 1
    operatorSet = set(['*', '/', '(', ')', '+', '-'])
    tokenList = inExpr.split()
    for token in tokenList:
        if token not in operatorSet:
            valueStack.append(token)
        elif(token == '('):
            opStack.append(token)
        elif(token == ')'):
            while(peek(opStack) != '('):
                temp1 = int(valueStack.pop())
                temp2 = int(valueStack.pop())
                tempOperator = opStack.pop()
                if(tempOperator == '*'):
                    valueStack.append(temp1 * temp2)
                elif(tempOperator == '/'):
                    valueStack.append(temp2 / temp1)
                elif(tempOperator == '+'):
                    valueStack.append(temp1 + temp2)
                elif(tempOperator == '-'):
                    valueStack.append(temp2 - temp1)
            opStack.pop()        
        else:
            while(not len(opStack) == 0 and opPrecedence[peek(opStack)] >= opPrecedence[token]):
                temp1 = int(valueStack.pop())
                temp2 = int(valueStack.pop())
                tempOp = opStack.pop()
                if(tempOp == '*'):
                    valueStack.append(temp1 * temp2)
                elif(tempOp == '/'):
                    valueStack.append(temp2 / temp1)
                elif(tempOp == '+'):
                    valueStack.append(temp1 + temp2)
                elif(tempOp == '-'):
                    valueStack.append(temp2 - temp1)
            opStack.append(token)       
    while(not len(opStack) == 0):
        temp1 = int(valueStack.pop())
        temp2 = int(valueStack.pop())
        tempOp = opStack.pop()
        if(tempOp == '*'):
            valueStack.append(temp1 * temp2)
        elif(tempOp == '/'):
            valueStack.append(temp2 / temp1)
        elif(tempOp == '+'):
            valueStack.append(temp1 + temp2)
        elif(tempOp == '-'):
            valueStack.append(temp2 - temp1)   
    temp3 = valueStack.pop()          
    return temp3


print(infixEvalOneCycle('100 * ( 2 + 12 ) / 14'))
                

            
            
            
           
       
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
