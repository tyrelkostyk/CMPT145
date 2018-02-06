# CMPT 145: Linear ADTs
# Post-fix arithmetic evaluation

# An application of the Stack ADT
# and the Queue ADT

import Queue as Queue
import Stack as Stack

example = "3 4 * 5 6 * +"

def evaluate(expr_string):
    '''
    Evaluate a postfix expression.
    Pre-conditions:
       expr_list: a list of numbers or strings representing arithemetic operations
    Post-Conditions:
        none
    Return:
        the value of the expression
    '''

    # create the initial empty data structures
    expression = Queue.create()
    evaluation = Stack.create()

    # put all the items in the Queue
    expr = expr_string.split()
    for c in expr:
        Queue.enqueue(expression, c)

    # brackets match iff every push has a corresponding pop
    while not Queue.is_empty(expression):
        c = Queue.dequeue(expression)

        if c.isdigit():
            Stack.push(evaluation, float(c))
        else:
            v1 = Stack.pop(evaluation)
            v2 = Stack.pop(evaluation)
            if c == '*':
                value = v1*v2
            elif c == '/':
                value = v2/v1
            elif c == '+':
                value = v1+v2
            elif c == '-':
                value = v2-v1
            else:
                print("syntax error")
                return None

            Stack.push(evaluation, value)

    return Stack.pop(evaluation)

print(evaluate(example))

value = 0
while value is not None:
    expr = input(">>")
    value = evaluate(expr)
    print(value)

print('goodbye')
