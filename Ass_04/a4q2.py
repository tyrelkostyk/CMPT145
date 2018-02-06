## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a4, due Friday Feb 9th 10pm

import TQueue as Queue
import TStack as Stack
import isfloat


def calculator(expression):
    '''
    Simple calculator that solves basic algbraic expressions involing the four main operators
    :params:
    expression - str, basic algbraic statement. REQUIRES parantheses around each operator and
        a space around each character
    :returns: numeric value, algebraic result of expression
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

    # Fill our stacks; evaluate
    while not Queue.is_empty(exprQueue):
        char = Queue.dequeue(exprQueue)
        if char in ('1','2','3','4','5','6','7','8','9','0'):
            Stack.push(numStack, char)
        elif char in ('+','-','*','/'):
            Stack.push(opStack, char)
        elif char == ')':
            num1 = float(Stack.pop(numStack))
            num2 = float(Stack.pop(numStack))
            op = Stack.pop(opStack)
            if op == '+':
                result = num1 + num2
                Stack.push(numStack, result)
            elif op == '-':
                result = num1 - num2
                Stack.push(numStack, result)
            elif op == '*':
                result = num1 * num2
                Stack.push(numStack, result)
            elif op == '/':
                result = num1 / num2
                Stack.push(numStack, result)

    return

example = '( 1 + 1 )'
calculator(example)
