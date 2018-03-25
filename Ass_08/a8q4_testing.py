## Tyrel Kostyk, tck290, 11216033
## CMPT145-04, Lab Section 04
## a8q3_testing.py


import treenode as tn
import treefunctions as tnfun
import a8q4


## Testing ordered()
test_ordered = [
    {'inputs'  : tn.create(5),
     'expected': True,
     'reason'  : 'single node, ordered'},
    {'inputs'  : tn.create(1, tn.create(6)),
     'expected': False,
     'reason'  : 'two node, h=2, Unorded Tree'},
    {'inputs'  : tn.create(1, None, tn.create(6)),
     'expected': True,
     'reason'  : 'two node, h=2, Osrded Tree'},
    {'inputs'  : tn.create(9, tn.create(2,  tn.create(1),
                                            tn.create(3) ),
                              tn.create(20, tn.create(10),
                                            tn.create(21) ) ),
     'expected': True,
     'reason'  : 'seven node, h=3, Ordered Tree'}
]

for t in test_ordered:
    args_in = t['inputs']
    expected = t['expected']

    result = a8q4.ordered(args_in)

    if result != expected:
        print('Error in ordered(): expected output', expected,
              'but found', result, '---', t['reason'])


print('*** Test Script Complete ***')
