## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a8q1_testing.py

import treenode as tn
import treefunctions as treefun
import exampletrees as extree
import a8q1

test_myFunction = [
    {'inputs' : [],
     'outputs': [],
     'reason' : 'Brief purpose/description'}
]

# loop over every test case in test_myFunction
for t in test_myFunction:
    args_in = t['inputs']
    expected = t['outputs']

    # initialize function data structure (if needed)
    thing = myScript.create()
    # use the inputs
    for val in args_in:
        myScript.add(thing, val)

    # now call your function
    result = myScript.myFunction(thing)

    if result != expected:
        print('Error in myFunction(): expected output', expected,
              'but found', result, '---', t['reason'])

print('*** Test Script Complete ***')
