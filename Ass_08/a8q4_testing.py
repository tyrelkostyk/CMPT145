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
    # {'inputs'  : tn.create(8, tn.create(5), tn.create(1)),
    #  'expected': True,
    #  'reason'  : 'three node, h=2, Complete Binary Tree'},
    # {'inputs'  : tn.create(3, tn.create(2, tn.create(9),
    #                                        tn.create(8) ),
    #                           tn.create(2, tn.create(7),
    #                                        tn.create(6) ) ),
    #  'expected': True,
    #  'reason'  : 'seven node, h=3, Complete Binary Tree'},
    # {'inputs'  : tn.create(15, tn.create(14, tn.create(12, tn.create(1),
    #                                                        tn.create(2)),
    #                                          tn.create(11, tn.create(3),
    #                                                        tn.create(4)) ),
    #                            tn.create(13, tn.create(10, tn.create(5),
    #                                                        tn.create(6)),
    #                                          tn.create(9,  tn.create(7),
    #                                                        tn.create(8)) ) ),
    #  'expected': True,
    #  'reason'  : 'fifteen node, h=4, Complete Binary Tree'},
]

for t in test_ordered:
    args_in = t['inputs']
    expected = t['expected']

    result = a8q4.ordered(args_in)

    if result != expected:
        print('Error in ordered(): expected output', expected,
              'but found', result, '---', t['reason'])


print('*** Test Script Complete ***')
