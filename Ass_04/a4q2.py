## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a4q2.py, due Friday Feb 9th 10pm

import TQueue as Queue
import TStack as Stack
import isfloat

def calculator(expression):
    '''
    Simple calculator that solves basic algbraic expressions involing the four main operators

    :params:
    expression - str, basic algbraic statement. REQUIRES parantheses around each operator and
        a space around each character

    :returns:
    result - float, algebraic result of expression
    '''
    # inintialize stacks, queues
    numStack = Stack.create()
    opStack = Stack.create()

    # Initialize & fill Queue with our expression's characters
    exprQueue = Queue.create()
    split_expr = expression.split()
    # print(split_expr)
    for char in split_expr:
        # print(char)
        Queue.enqueue(exprQueue, char)

    # Fill the stacks; evaluate
    while not Queue.is_empty(exprQueue):
        char = Queue.dequeue(exprQueue)
        # If char is a number, push onto the numStack
        if isfloat.isfloat(char):
            Stack.push(numStack, char)
        # If char is an operation, push onto the opStack
        elif char in ('+','-','*','/'):
            Stack.push(opStack, char)
        # If char is ')', perform operation between next 2 values using next operation
        elif char == ')':
            num2 = float(Stack.pop(numStack))
            num1 = float(Stack.pop(numStack))
            op = Stack.pop(opStack)
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2
            Stack.push(numStack, result)

    result = Stack.pop(numStack)
    return result
