## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a4q3.py, due Friday Feb 9th 10pm

import a4q2

print('Welcome to the calculator. Begin calculating, or type quit to exit.')

while True:
    expression = input('Enter a valid algebraic expression: ')
    if expression == quit:
        print('Exiting calculator.')
        break
    elif expression != 'quit':
        result = a4q2.calculator(str(expression))
        print(result)
