## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a4q2_testing, due Friday Feb 9th 10pm

import a4q2

test_calculator = [
    {'inputs' : '( 1 + 1 )',
     'outputs': 2.0,
     'reason' : 'simple addition'},
    {'inputs' : '( 5 - 4 )',
     'outputs': 1.0,
     'reason' : 'simple subtraction'},
    {'inputs' : '( 7 * 4 )',
     'outputs': 28.0,
     'reason' : 'simple multiplication'},
    {'inputs' : '( 10 / 5 )',
     'outputs': 2.0,
     'reason' : 'simple division'},
    {'inputs' : '(((( 3 + 4 ) - 1 ) * 2 ) / 3 )',
     'outputs': 4.0,
     'reason' : 'simple use of every operation'},
    {'inputs' : '((((( 5 * 3 ) - 3 ) * 4 ) + 12 ) / 3 )',
     'outputs': 20.0,
     'reason' : 'slightly more complicated use of every operation'}
]

for i in test_calculator:
    args_in = i['inputs']
    expected = i['outputs']

    # now call calculator()
    result = a4q2.calculator(args_in)

    # finally, check the result of count()
    if result != expected:
        print('Error in calculator(): expected value', expected,
              ' but found ', result, '---', i['reason'])

print('*** Test script completed ***')
