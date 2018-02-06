## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a4q1.py, due Friday Feb 9th 10pm

import TStack as Stack
import sys

# Initialize Stacks
lineStack = Stack.create()
wordStack = Stack.create()

# Read file
file = open(sys.argv[1])

# Push each line onto lineStack
for line in file:
    Stack.push(lineStack, line)

# Reverse the order of words w/in each line, then print each line in reverse order
while not Stack.is_empty(lineStack):
    result = ''
    line = Stack.pop(lineStack)
    x = line.split()
    for words in x:
        Stack.push(wordStack, words)
    while not Stack.is_empty(wordStack):
        result += str(Stack.pop(wordStack))+' '
    print(result)

file.close()
