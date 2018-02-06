## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a4, due Friday Feb 9th 10pm

import TStack as Stack
import sys


lineStack = Stack.create()
wordStack = Stack.create()

file = open(sys.argv[1])

for line in file:
    Stack.push(lineStack, line)

while not Stack.is_empty(lineStack):
    line = Stack.pop(lineStack)
    x = line.split()
    for words in x:
        Stack.push(wordStack, words)
    while not Stack.is_empty(wordStack):
        print(Stack.pop(wordStack))

file.close()
